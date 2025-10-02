import logging

import requests

from .errors import BadRequest, Unauthorised, Forbidden, TooManyRequests, NotFound
from .urls import URLs


#Fetches response from the relevant endpoints and applies parameters to the request as needed are needed
class API(URLs):

    def __init__(self):
        super().__init__()

    #Method handles error codes from the API
    def _response_code_error_type(self, resp):
        if resp.status_code == 400:
            raise BadRequest(response=resp)
        if resp.status_code == 401:
            raise Unauthorised(response=resp)
        if resp.status_code == 403:
            raise Forbidden(response=resp)
        if resp.status_code == 404:
            raise NotFound(response=resp)
        if resp.status_code == 429:
            raise TooManyRequests(response=resp)


    def make_request(self, endpoint: str=None, params: dict={}) -> str:

        logging.debug(msg=f'Fetching resp from endpoint: {endpoint} with params: {params}')

        try:
            response = requests.get(url=endpoint, params=params)

            if response.status_code != 200:
                self._response_code_error_type(response)

            logging.debug(msg=f'Returning resp from endpoint: {endpoint} with params: {params}')
            return response

        except Exception as err:
            logging.error(msg=err, exc_info=True)
            raise
