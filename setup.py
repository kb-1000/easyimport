# Copyright 2016-2018 Kaeptm Blaubaer
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#end-license-header

import io


with io.open("README.rst", "rt", encoding="utf-8") as fp:
    long_description = fp.read()

from setuptools import setup


setup(name="easyimport",
      version="0.91",
      py_modules=["easyimport"],
      author="Kaeptm Blaubaer",
      author_email="kaeptmblaubaer1000@gmail.com",
      description="Lazy importer for speeding up the import system",
      long_description=long_description,
      url="https://github.com/kaeptmblaubaer1000/easyimport/",
      download_url="https://github.com/kaeptmblaubaer1000/easyimport/archive/stable.zip",
      install_requires=[
          "six>=1.11.0",
      ],
)
