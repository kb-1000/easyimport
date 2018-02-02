from __future__ import unicode_literals, absolute_import
import sys
from importlib import import_module as __import__
from functools import partial as _partial

modules = {}
__all__ = ["EasyImporter", "easyimporter", "modules"]
_special = ["__call__", "__str__", "__add__", "__radd__"]

def _EasyImporter___setattr__(self, attr, val):
  if self.obj is not None:
   setattr(self.obj, attr, val)
  else:
   sys.modules[attr] = val

def name(obj):
 if hasattr(obj, "__qualname__"):
  return str(obj.__qualname)
 elif hasattr(obj, "__module__"):
  if not hasattr(obj, "__name__"):
   raise ValueError("Invalid name composition (__module__ but not __name__)")
  else:
   return str(obj.__module__).rstrip(".") + "." + str(obj.__name__).lstrip(".")
 elif hasattr(obj, "__name__"):
  return str(obj.__name__)

try:
 unicode
except NameError:
 _str = str
 _bytes = bytes
else:
 _bytes = str
 _str = unicode

def EasyImporter(prefix=""):
 if type(prefix) != _str:
  try:
   prefix = _str(prefix)
  except:
   raise TypeError("prefix must be a string")
 if prefix in modules:
  return modules[prefix]
 else:
  importer = _EasyImporter(prefix)
  modules[prefix] = importer
  return importer


class _EasyImporter:
 def __init__(self, prefix=""):
  self.prefix = prefix
  if prefix:
   self.obj = __import__(prefix)
   for s in _special:
    if hasattr(self.obj, s):
     setattr(self, s, _partial(getattr(self.obj, s), self.obj))
  else:
   self.obj = None
  self.__setattr__ = _partial(_EasyImporter___setattr__, self)
 
 def __getattr__(self, attr):
  if self.obj is not None:
   if hasattr(self.obj, attr):
    return getattr(self.obj, attr)
   else:
    return EasyImporter(self.prefix + "." + attr)
  else:
   return EasyImporter(attr)
 
 def __repr__(self):
  if self.obj is not None:
   if not hasattr(self.obj, "__repr__"):
    return repr(self.obj)
   else:
    r = self.obj.__repr__
    if isinstance(r, type(EasyImporter)):
     return r()
    else:
     return r()
  else:
   return "<EasyImporter at %s>" % hex(id(self))
 
 def __call__(self, *args, **kwargs):
  if hasattr(self.obj, "__call__"):
   self.obj.__call__(self.obj)
  elif hasattr(self.obj, "__name__"):
   raise TypeError("Module %s is not callable" % repr(self.obj.__name__))
  else:
   if isinstance(self.obj, type):
    raise TypeError("'%s' object is not callable" % name(type(self.obj)))
 def __radd__(self, s):
  return s + self.obj
 
_EasyImporter.__name__ = "EasyImporter"
easyimporter = EasyImporter()

if __name__ == "__main__":
 print(easyimporter)
 print(easyimporter.sys)