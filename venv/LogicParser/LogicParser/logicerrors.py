# Author: Ted Janney
# Date: 16/11/2020
# Description: A class of warnings and errors specific to logic evaluation and the LogicParser interface

class LogicErrors():
    '''
    This class is meant to primarily deliver warnings or error messages to the screen, instead of an exception,
    so the program can just simply move on to asking for more input.

    Data members - each one should be named for the action that caused the error:
        Public:


        Private:
            A dictionary or map with error codes and the verbose error it should return

    Methods:
        Public:
            get_error(some_string_error_description)
        Private:
            check_for_errors(some_string_error_description) -> dictionary or map to look up error codes and match
                errors.
            undefined_error(some_string_error_description) -> if check_for_errors() doesn't have a key with the passed
                error code, it throws an undefined error.


    '''
    def __init__(self, error_code):
        self._error_code = error_code
        self.wrong_input = "\n\nYou have attempted unrecognized input. Type -h for help or -u for usage.\n\n"

    def get_error(self, error_code):
        return self.wrong_input

print(LogicErrors("Wrong Input").wrong_input)