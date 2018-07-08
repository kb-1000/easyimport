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
