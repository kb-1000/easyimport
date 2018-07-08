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
