# Exception definitions

from httplib import BAD_REQUEST


class ApiException(Exception):
    """
    The Base exception class for controller level exceptions
    """

    def __init__(self, message, code=500):
        self.code = code
        self.message = message

    def __str__(self):
        return '{}: {}'.format(self.code, self.message)

    def description_as_dict(self):
        return dict(message=self.message)


class InvalidInputException(ApiException):
    """ Input parameters validation errors exception """

    def __init__(self, errors):
        self.code = BAD_REQUEST
        self.message = 'Invalid input parameters'
        self.errors = errors

    def description_as_dict(self):
        return dict(message=self.message, errors=self.errors)