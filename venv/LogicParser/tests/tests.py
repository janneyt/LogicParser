import unittest
from LogicParser.LogicParser.logicparser import LogicParser, get_input


class LogicParserExists(unittest.TestCase):

    def setUp(self):
        self.func = LogicParser('T')

    def test_begin_parsing_exists(self):
        self.assertEquals(LogicParser.begin_parsing(self, 'T -tt'),'T')

    def test_begin_parsing_single_false(self):
        self.assertEquals(LogicParser.begin_parsing(self, 'F -tt'),'F')

    def test_begin_parsing_wrong_input(self):
        self.assertEquals(LogicParser.begin_parsing(self, True), get_input())

    def test_begin_parsing_wrong_characters(self):
        self.assertEquals(LogicParser.begin_parsing(self, 'TL -tt'),"The only valid truth table values are T and F. Please make sure to adhere to these guidelines.")


if __name__ == '__main__':
    unittest.main()
