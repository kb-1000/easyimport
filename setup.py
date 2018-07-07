import io


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
      description="Lazy importer for speeding up the import system",
      long_description=long_description,
      url="https://github.com/kaeptmblaubaer1000/easyimport/",
      download_url="https://github.com/kaeptmblaubaer1000/easyimport/archive/stable.zip",
)
