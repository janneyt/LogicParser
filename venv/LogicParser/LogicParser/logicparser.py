# Author: Ted Janney
# Date: 15/11/2020
# Description: A parser module that produces truth tables.

# TODO: Add a parsing module to pass the message to begin_parsing

# TODO: Create all warnings/errors as a global object class using pythonic patterns.

class LogicParser(object):
    '''
    This class contains the current truth values being evaluated as well as their eventual answer.


    '''

    def __init__(self, message):
        '''

        '''
        self._message = message
        self._wrong_letter = "The only valid truth table values are T and F. Please make sure to adhere to these guidelines."
        self._warning = "Something has gone wrong. Please be advised that you have passed some form of wrong input."


    def begin_parsing(self, message):
        '''
        Takes an object, the current truth query, and assigns it to the correct module of the program.

        >>> LogicParser.begin_parsing(LogicParser('T -tt'),'T -tt')
        'T'

        >>> parse_list = ['T -tt', 'F -tt']
        >>> [LogicParser.begin_parsing(LogicParser('T -tt'), x) for x in parse_list]
        ['T','F']

        >>> LogicParser.begin_parsing(LogicParser('T'), 'T')
        'You are missing a command code. If you do not know what code to use, please type -h into the
        console.'

        >>> LogicParser.begin_parsing(LogicParser('T'),True)
        Traceback (most recent call last):
        ...
        TypeError:

        Object, String -> String
        :return: a string
        '''
        string_message = isinstance(message, str)
        if string_message:
            return 'T'
        else:
            get_input()

def get_input():
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()