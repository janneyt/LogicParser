# Author: Ted Janney
# Date: 15/11/2020
# Description: A parser module that produces truth tables.

# TODO: Add a parsing module to pass the message to begin_parsing

class LogicParser(object):
    '''
    This class contains the current truth values being evaluated as well as their eventual answer.


    '''

    def __init__(self, message):
        '''

        '''
        self._message = message
        self._warning = "Something has gone wrong. Please be advised that you have passed some form of wrong input."


    def begin_parsing(self):
        '''
        Takes an object, the current truth query, and assigns it to the correct module of the program.

        Object -> Function (or object.method)
        :return: a function call
        '''
        pass

