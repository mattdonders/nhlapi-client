import logging

import requests

from nhlapi.api import teams, schedule

NHL_API_BASE_URL = "https://statsapi.web.nhl.com/api/v1"
REUSABLE_SESSION = requests.Session()


class NHLAPIClient:
    """ A standard HTTP REST client ussed by the NHL API class. """

    def __init__(self, host, **kwargs):
        self.host = host
        self._client_kwargs = kwargs
        self.session = requests.Session()

    def execute(self, path, **kwargs):
        """ Executes a GET request to the given endpoint, returning the result. """

        url = f"{self.host}/{path}"
        logging.info(url)
        kwargs.update(self._client_kwargs)

        session = self.session
        retries = requests.adapters.HTTPAdapter(max_retries=3)
        session.mount("https://", retries)
        session.mount("http://", retries)

        response = session.get(url, **kwargs)
        return response


class NHLAPI:
    def __init__(self, host=NHL_API_BASE_URL, client=NHLAPIClient, **kwargs):
        self.client = client(host=host, **kwargs)
        self.teams = teams.API(self.client)
        self.schedule = schedule.API(self.client)
