from nhlapi.api import APIEndpoint

from nhlapi.models.people import Person


class API(APIEndpoint):
    def __init__(self, api, endpoint="people"):
        super(API, self).__init__(api, endpoint=endpoint, cls=Person)

    def get(self, person_id=None, **kwargs):
        """ Gets the details for one NHL Player (Person). """

        endpoint = f"{self.endpoint}/{person_id}"

        return super(API, self).get(endpoint=endpoint, **kwargs)
