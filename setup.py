import io

try:
    import urlparse
    import urllib
except ImportError:
    import urllib.parse as urlparse
    import urllib.request as urllib

from distutils.config import PyPIRCCommand as p
p.DEFAULT_REPOSITORY = "https://pypi.python.org/pypi/"

_urlparse = urlparse.urlparse
def parseurl(url, *args, **kwargs):
 p = _urlparse(url, *args, **kwargs)
 if p.scheme == "http":
  l = list(p.geturl())
  l.insert(4, "s")
  p = _urlparse("".join(l))
 return p
urlparse.urlparse = parseurl

del parseurl, urlparse, urllib

with io.open("README.rst", "rt", encoding="utf-8") as fp:
    long_description = fp.read()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="easyimport",
      version="0.91",
      py_modules=["easyimport"],
      author="Kaeptm Blaubaer",
      author_email="kaeptmblaubaer1000@gmail.com",
      description="Easy Importer for speeding up the import system",
      long_description=long_description,
      url="https://github.com/kaeptmblaubaer1000/easyimport/",
      download_url="https://github.com/kaeptmblaubaer1000/easyimport/archive/stable.zip",
)