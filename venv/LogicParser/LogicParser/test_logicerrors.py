import unittest
from LogicParser.LogicParser.logicerrors import LogicErrors

class WarningClassExists(unittest.TestCase):
    def setUp(self):
        self.func = LogicErrors("Wrong Input")

    def test_LogicErrorsRequiresErrorCode(self):
        self.assertTrue(LogicErrors("Wrong Input"))

    def test_LogicErrorsRequiredErrorCode(self):
        logic_error = LogicErrors("Wrong Input")
        self.assertTrue(logic_error.get_error("Wrong Input"))

    def test_LogicErrorsWrongInputErrorExists(self):
        logic_error = LogicErrors("Wrong Input")
        # So I'm just testing the existing of the wrong_input error message
        self.assertTrue(logic_error.wrong_input)

    def test_LogicErrorsWrongInputReturnsWarning(self):
        logic_error = LogicErrors("Wrong Input")
        self.assertEqual(logic_error.get_error("Wrong Input"), logic_error.wrong_input)


if __name__ == '__main__':
    unittest.main()