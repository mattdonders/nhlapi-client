from nhlapi.api import APIEndpoint

from nhlapi.models.schedule import Schedule


class API(APIEndpoint):
    def __init__(self, api, endpoint="schedule"):
        super(API, self).__init__(api, endpoint=endpoint, cls=Schedule)

    def get(self, **kwargs):
        """ Gets the details for one or more campaigns by ID """

        endpoint = self.endpoint
        return super(API, self).get(endpoint=endpoint, **kwargs)

    def get_fully_expanded(self, **kwargs) -> Schedule:
        """ Gets the details for one or more campaigns by ID """

        endpoint = self.endpoint
        kwargs.update({"expand": "schedule.broadcasts,schedule.teams,schedule.linescore,"})
        return super(API, self).get(endpoint=endpoint, **kwargs)
