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

license_header = """\
Copyright 2016-2018 Kaeptm Blaubaer

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.\
"""

import logging
import os
import sys
import textwrap


lambda_True = lambda *a, **k: True
logger = logging.getLogger("update_license_headers")


class FiletypeNotInRegistryError(Exception):
    pass


def indent(text, indentation, cond):
    return "\n".join(((indentation + line) if cond(line) else line) for line in text.split("\n"))

def hash_comment(text):
    return indent(text, "# ", lambda_True)


filetype_registry = {
    ".cfg": (hash_comment, "#end-license-header\n"),
    ".gitattributes": (hash_comment, "#end-license-header\n"),
    ".gitignore": (hash_comment, "#end-license-header\n"),
    ".in": (hash_comment, "#end-license-header\n"),
    ".py": (hash_comment, "#end-license-header\n"),
    # TODO: ReStructuredText
}


def update_file(filename):
    file, ext = os.path.splitext(filename)
    if not ext:
        ext = file
    if ext not in filetype_registry:
        raise FiletypeNotInRegistryError(ext)
    filetype = filetype_registry[ext]
    shebang = ""
    with open(filename, "rt", encoding="utf-8") as fp:
        if fp.read(2) == "#!":
            shebang = "#!" + fp.readline()
        else:
            fp.seek(0)

        text = fp.read()
    if filetype[1] in text:
        text = text.partition(filetype[1])[2]
    licensed_text = shebang + filetype[0](license_header) + "\n" + filetype[1] + "\n" + text.lstrip()
    with open(filename, "wt", encoding="utf-8") as fp:
        fp.write(licensed_text)


def should_have_header(filename):
    # Compiled Python files
    if filename.endswith(".pyc") or filename.endswith(".pyo"):
        return False
    # The license is not my work
    if filename.endswith(os.sep + "LICENSE") or filename == "LICENSE":
        return False
    # Overwriting files in the build directory is the task of setup.py build
    if filename.endswith(os.sep + "build") or filename == "build":
        return False
    if filename.endswith(".egg-info") or filename.endswith(".dist-info"):
        return False
    # setup_requires cache
    if filename.endswith(".egg") or filename.endswith(".eggs"):
        return False
    if filename.endswith(os.sep + "dist") or filename == "dist":
        return False
    if filename.endswith(".git"):
        return False
    return True


def flat_walk(path, filter_func=lambda_True):
    for root, directories, files in os.walk(path):
        for directory in directories[:]:
            directory_path = os.path.normpath(os.path.join(root, directory))
            if not filter_func(directory_path):
                directories.remove(directory)

        for file in files:
            file_path = os.path.normpath(os.path.join(root, file))
            if filter_func(file_path):
                yield file_path


def main():
    path = os.path.normpath(os.path.join(__file__, ".."))
    for file in flat_walk(path, should_have_header):
        try:
            update_file(file)
        except FiletypeNotInRegistryError as e:
            logger.warn("The file {0} is using the filetype {1}. This program is unable to process it.".format(file, e))


if __name__ == "__main__":
    main()
