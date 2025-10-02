from .api import API

class Wrapper(API):

    def __init__(self):
        super().__init__()

    #Enter the name of a given endpoint as arguement and recieve the endpoint as return
    def _fetch_endpoint(self, endpoint_name: str=None) ->str:

        if endpoint_name == 'legislation':
            return self._legislation_url()
        if endpoint_name == 'debates':
            return self._debates_url()
        if endpoint_name == 'constituencies':
            return self._constituencies_url()
        if endpoint_name == 'parties':
            return self._parties_url()
        if endpoint_name == 'divisions':
            return self._divisions_url()
        if endpoint_name == 'questions':
            return self._questions_url()
        if endpoint_name == 'houses':
            return self._houses_url()
        if endpoint_name == 'members':
            return self._members_url()

    def wrapper_make_request(self, endpoint_name: str=None, params: dict={}) ->str :

        #Fetch the actual endpoint url to use
        correct_endpoint = self._fetch_endpoint(endpoint_name=endpoint_name)

        #Make call the the API for response
        response = self.make_request(endpoint=correct_endpoint, params=params)

        return response