import easyimport
from easyimport import easyimporter as e, modules, EasyImporter
import unittest

class CacheTest(unittest.TestCase):
    def test_sys(self):
        self.assertIs(e.sys, e.sys)

    def test_constructor(self):
        self.assertIs(EasyImporter(), EasyImporter())
