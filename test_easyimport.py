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

import easyimport
from easyimport import easyimporter as e, modules, EasyImporter
import unittest

class CacheTest(unittest.TestCase):
    def test_sys(self):
        self.assertIs(e.sys, e.sys)

    def test_constructor(self):
        self.assertIs(EasyImporter(), EasyImporter())

    def test_six(self):
        self.assertIs(e.six, e.six)

    def test_six_moves(self):
        self.assertIs(e.six.moves, e.six.moves)

    def test_six_moves_urllib(self):
        self.assertIs(e.six.moves.urllib, e.six.moves.urllib)

    def test_easyimporter(self):
        self.assertIs(e, EasyImporter())


class TypeTest(unittest.TestCase):
    def test_sys(self):
        self.assertIsInstance(e.sys, EasyImporter)

    def test_constructor(self):
        self.assertIsInstance(EasyImporter(), EasyImporter)

    def test_easyimporter(self):
        self.assertIsInstance(e, EasyImporter)

    def test_six(self):
        self.assertIsInstance(e.six, EasyImporter)

    def test_six_moves(self):
        self.assertIsInstance(e.six.moves, EasyImporter)

    def test_six_moves_urllib(self):
        self.assertIsInstance(e.six.moves.urllib, EasyImporter)

    def test_sys_modules(self):
        self.assertNotIsInstance(e.sys.modules, EasyImporter)
