import jinja2

import itertools
import json
import os
import pathlib
import types

def intersect(l0, l1):
  return sorted(frozenset(l0) & frozenset(l1))

def filterout(l0, l1):
  return sorted(frozenset(l1) - frozenset(l0))

def out_of_date(target, source):
  if not os.path.exists(target):
    return True
  if not os.path.exists(source):
    return True
  ttime = os.path.getmtime(target)
  if ttime < os.path.getmtime(source):
    return True
  if os.path.isdir(source):
    # if target is a directory, check all subdir modtimes too
    for p, dd, _ in os.walk(source):
      for d in dd:
        if ttime < os.path.getmtime(os.path.join(p, d)):
          return True
  return False

class BuildConfig(object):
  """Tracks which files and directories we scanned to configure the build.

  This helps the meta-build avoid walking the whole directory tree every time.
  """
  def __init__(self):
    self.used_files = {}
    self.used_dirs = {}

  def used(self):
    return itertools.chain(self.used_files.keys(), self.used_dirs.keys())

  def open(self, file, *args, **kwargs):
    self.used_files[file] = None
    return open(file, *args, **kwargs)

  def walk_files(self, base):
    self.used_dirs[base] = None
    for p, _, ff in os.walk(base):
      for f in ff:
        yield os.path.join(p, f)

  def walk_dirs(self, base):
    self.used_dirs[base] = None
    if os.path.isdir(base):
      yield base
    for p, dd, _ in os.walk(base):
      for d in dd:
        yield os.path.join(p, d)

  def rel_vars(self, bases, path):
    p = pathlib.Path(path)
    for n, d in bases.items():
      dp = pathlib.Path(d)
      if dp == p or dp in p.parents:
        rp = os.path.relpath(p, d)
        return "$"+n if rp == "." else os.path.join("$"+n, rp)
    return path

  def examine_deps(self, ctx, extra_dirs=[]):
    bases = {}
    # figure out which variables correspond to which used directories
    for u in list(self.used_dirs.keys()) + extra_dirs:
      for k, v in ctx.items():
        if u == v:
          bases[k] = v
    # to depend on a directory means to depend on the list of files of that directory (and its subdirs)
    # ninja doesn't apply recursion logic to directory dependencies, so we do it here
    return [self.rel_vars(bases, d)
      for x in self.used()
      for d in (self.walk_dirs(x) if os.path.isdir(x) else [x])]

  def collect_config(self, local_, global_, global_filter=lambda _: True, extra_dirs=[]):
    ctx = {
      k: v
      for k, v in global_.items()
      if k.isupper() and global_filter(k)
    } | {
      k: v
      for k, v in local_.items()
      if k.isupper() and not callable(v)
    }
    ctx["CONFIGURE_DEPS"] = self.examine_deps(ctx, extra_dirs=extra_dirs)
    return ctx

def nj_q(f, var=True):
  """Quote function for the body of a ninja rule.

  # https://ninja-build.org/manual.html#ref_lexer
  """
  if var and f[0] == "$":
    # don't escape values that start with a ninja variable
    return "$" + f[1:].replace("$", "$$").replace("\n", "$\n")
  else:
    return f.replace("$", "$$").replace("\n", "$\n")

def nj_qi(f):
  """Quote function for the inputs of a ninja rule.

  # https://ninja-build.org/manual.html#ref_lexer
  """
  return nj_q(f).replace(" ", "$ ")

def nj_qo(f):
  """Quote function for the outputs of a ninja rule.

  # https://ninja-build.org/manual.html#ref_lexer
  """
  return nj_qi(f).replace(":","$:")

def njinjify(j2env, depfile=None):
  j2env.filters |= {
    "nj_q": nj_q,
    "nj_qi": nj_qi,
    "nj_qo": nj_qo,
  }
  j2env.globals |= {
    "path_exists": os.path.exists,
    "path_join": os.path.join,
    "relpath": os.path.relpath,
    "map": map,
    "zip": zip,
  }

  if depfile:
    # monkeypatch j2env to track dependencies on other files
    # TODO: drop after https://github.com/pallets/jinja/pull/1776
    j2env._parsed_names = []
    old_parse = j2env._parse
    def _parse(self, source, name, filename):
      if name is not None:
          self._parsed_names.append(name)
      return old_parse(source, name, filename)
    j2env._parse = types.MethodType(_parse, j2env)
  return j2env

class FileLoader(jinja2.BaseLoader):
  def get_source(self, env, tpl):
    mtime = os.path.getmtime(tpl)
    with open(tpl) as fp:
      return (fp.read(), tpl, lambda: mtime == os.path.getmtime(tpl))

def run_j2(infile, ctx, outfile, depfile=None, outjson=None, j2env=None, headers=None):
  j2env = j2env or jinja2.Environment()
  njinjify(j2env, depfile=depfile)

  if outjson:
    with open(outjson, "w") as fp:
      json.dump(ctx, fp, indent=2)

  result = j2env.overlay(loader=FileLoader()).get_template(infile).render(ctx)

  with open(outfile, 'w') as fp:
    if headers:
      for h in headers:
        fp.writelines(["# ", h, "\n"])
      fp.write("\n")
    # jinja templates strip trailing newline by default so we need print
    print(result, file=fp)

  if depfile:
    deps = j2env._parsed_names
    assert deps[0] == infile
    with open(depfile, 'w') as fp:
      print("%s: %s" % (outfile, " ".join(deps)), file=fp)

def mk_ninja(infile, cfg, builddir, outfile=None, depfile=None, cfgfile=None, headers=None):
  basename = os.path.splitext(os.path.basename(infile))[0]
  outfile = outfile or os.path.join(builddir, basename)
  depfile = depfile or os.path.join(builddir, basename+".d")
  cfgfile = cfgfile or os.path.join(builddir, basename+".json")
  headers = headers if headers is not None else [
    "This file was automatically generated. ANY EDITS WILL BE LOST.",
    "",
    "template: %s" % os.path.relpath(infile, builddir),
    "variables: %s" % os.path.relpath(cfgfile, builddir),
  ]
  os.makedirs(builddir, exist_ok=True)
  run_j2(
    infile, cfg, outfile,
    outjson=cfgfile,
    depfile=depfile,
    headers=headers)
