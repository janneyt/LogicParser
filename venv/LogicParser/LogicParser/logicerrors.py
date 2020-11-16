# Author: Ted Janney
# Date: 16/11/2020
# Description: A class of warnings and errors specific to logic evaluation and the LogicParser interface

class LogicErrors():
    '''
    This class is meant to primarily deliver warnings or error messages to the screen, instead of an exception,
    so the program can just simply move on to asking for more input.

    Data members - each one should be named for the action that caused the error:
        Private:
            A dictionary or map with error codes and the verbose error it should return

    Methods:
        Public:
            get_error(some_string_error_description)



    '''
    def __init__(self, error_code):
        self._error_code = error_code

        '''
        Below is the error dictionary that makes this whole class worthwhile.
        
        PLEASE UPDATE.
        '''
        self.error_dict = {
            "wrong input": "\n\nYou have attempted unrecognized input. Type -h for help or -u for usage.\n\n",
            "not recognized": "\n\nHey! Whatever you just did is an unrecognized error. Pathetic.\n\n"
        }
    def get_error(self, error_code):
        try:
            return self.error_dict[error_code.lower()]

        # The exception handling is designed to just pass an error code back. In this way, no matter what the
        # function returns a string. However, if other code is for some reason relying on this error handling to
        # fail, it won't. Thus, always expect a message back.
        except Exception as e:
            if type(e) is KeyError:
                return self.error_dict["not recognized"]
            elif type(e) is AttributeError:
                return self.error_dict["not recognized"]
            return e
