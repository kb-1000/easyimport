from __future__ import unicode_literals, absolute_import
import sys
from importlib import import_module as _import_module
from functools import partial as _partial

try:
    modules.clear()
except NameError:
    modules = {}

__all__ = ["EasyImporter", "easyimporter", "modules"]
_special = ["__call__", "__str__", "__add__", "__radd__"]

def _EasyImporter___setattr__(self, attr, val):
    if self.__obj is not None:
        setattr(self.__obj, attr, val)
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

import six as _six

_str = _six.text_type
_bytes = _six.binary_type

class _EasyImporterMeta(type):
    def __call__(cls, prefix=""):
        if not isinstance(prefix, _str):
            try:
                prefix = _str(prefix)
            except Exception:
                raise TypeError("prefix must be a string")
        if prefix in modules:
            return modules[prefix]
        else:
            importer = super(_EasyImporterMeta, cls).__call__(prefix)
            modules[prefix] = importer
            return importer


class EasyImporter(_six.with_metaclass(_EasyImporterMeta, object)):
    def __init__(self, prefix=""):
        self.__prefix = prefix
        if prefix:
            self.__obj = _import_module(prefix)
            for s in _special:
                if hasattr(self.__obj, s):
                    setattr(self, s, _partial(getattr(self.__obj, s), self.__obj))
        else:
            self.__obj = None
        self.__setattr__ = _partial(_EasyImporter___setattr__, self)

    def __getattr__(self, attr):
        if self.__obj is not None:
            if hasattr(self.__obj, attr):
                return getattr(self.__obj, attr)
            else:
                return EasyImporter(self.__prefix + "." + attr)
        else:
            return EasyImporter(attr)

    def __repr__(self):
        if self.__obj is not None:
            if not hasattr(self.__obj, "__repr__"):
                return repr(self.__obj)
            else:
                r = self.__obj.__repr__
                if isinstance(r, type(EasyImporter)):
                    return r()
                else:
                    return r()
        else:
            return "<EasyImporter at %s>" % hex(id(self))

    def __call__(self, *args, **kwargs):
        if hasattr(self.__obj, "__call__"):
            self.__obj.__call__(self.__obj)
        elif hasattr(self.__obj, "__name__"):
            raise TypeError("Module %s is not callable" % repr(self.__obj.__name__))
        else:
            if isinstance(self.__obj, type):
                raise TypeError("'%s' object is not callable" % name(type(self.__obj)))

    def __radd__(self, s):
        return s + self.__obj


easyimporter = EasyImporter()

if __name__ == "__main__":
    print(easyimporter)
    print(easyimporter.sys)
    print(type(easyimporter.six.moves))
