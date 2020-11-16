import unittest
from LogicParser.LogicParser.logicparser import LogicParser

class LogicParserExists(unittest.TestCase):

    def setUp(self):
        self.func = LogicParser('T')

    def test_begin_parsing_exists(self):
        self.assertEquals(LogicParser.begin_parsing('T -tt'),'T')

    def test_begin_parsing_single_false(self):
        self.assertEquals(LogicParser.begin_parsing('F -tt'),'F')


if __name__ == '__main__':
    unittest.main()
