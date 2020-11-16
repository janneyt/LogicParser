import unittest
from LogicParser.LogicParser.logicerrors import LogicErrors

class WarningClassExists(unittest.TestCase):
    def setUp(self):
        self.func = LogicErrors("Wrong Input")

    def test_LogicErrorsRequiresErrorCode(self):
        self.assertTrue(LogicErrors("Wrong Input"))

    def test_LogicErrorsRequiredErrorCode(self):
        logic_error = LogicErrors("Wrong Input")
        self.assertTrue(logic_error.get_error("wrong input"))

    def test_LogicErrorsWrongInputErrorExists(self):
        logic_error = LogicErrors("Wrong Input")
        # So I'm just testing the existing of the wrong_input error message
        self.assertTrue(logic_error.error_dict["wrong input"])

    def test_LogicErrorsWrongInputReturnsWarning(self):
        logic_error = LogicErrors("Wrong Input")
        self.assertEqual(logic_error.get_error("wrong input"), logic_error.error_dict["wrong input"])

    def test_LogicErrorsWrongInputCapitalization(self):
        logic_error = LogicErrors("Wrong Input")
        self.assertEqual(logic_error.get_error("wrong Input"), logic_error.error_dict["wrong input"])

    def test_LogicErrorsWrongInputInteger(self):
        logic_error = LogicErrors("wrong input")
        self.assertRaises(TypeError, logic_error.get_error(1))

    def test_LogicErrorsWrongInputNonexistentCode(self):
        logic_error = LogicErrors("wrong input")
        self.assertEqual(logic_error.get_error("all the elephants must die"), logic_error.get_error("not recognized"))

    def test_LogicErrorsWrongInputNone(self):
        logic_error = LogicErrors("wrong input")
        self.assertEqual(logic_error.get_error(None), logic_error.get_error("not recognized"))

    def test_LogicErrorsErrorDictionaryExists(self):
        logic_error = LogicErrors("Wrong Input")
        self.assertTrue(logic_error.error_dict)


if __name__ == '__main__':
    unittest.main()