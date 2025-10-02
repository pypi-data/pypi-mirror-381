class OireachtasAPIException(Exception):
    """Baseline exception class for the Oireachtas API"""
    pass

class HTTPException(OireachtasAPIException):

    # Created with the defaults of none so that we can later cover json and HTTPS exceptions in the one area
    def __init__(self, response=None, response_json=None):
        self.response = response

        self.api_error = []
        self.api_code = []
        self.api_message = []

        try:
            status_code = response.status.code
        except AttributeError:
            # Response is an instance of http.clientresponse
            status_code = response.status

class BadRequest(HTTPException):
    """BadRequest()
    Exception raised for a 400 HTTP status code
    """
    pass

class Unauthorised(HTTPException):
    """Unauthorised()
    Exception raise for a 401 HTTP status code
    """
    pass

class Forbidden(HTTPException):
    """Forbidden()
    Exception raise for a 404 HTTP status code
    """
    pass

class TooManyRequests(HTTPException):
    """TooManyRequests()
    Exception raised for a 429 HTTP status code
    """
    pass

class NotFound(HTTPException):
    """NotFound()
    Exceotion riasaed for a 404 HTTP status code
    """
    pass