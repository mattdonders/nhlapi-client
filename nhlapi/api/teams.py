from nhlapi.api import APIEndpoint

from nhlapi.models.teams import Teams


class API(APIEndpoint):
    def __init__(self, api, endpoint="teams"):
        super(API, self).__init__(api, endpoint=endpoint, cls=Teams)

    def get(self, team_id=None, **kwargs):
        """ Gets the details for one or more campaigns by ID """

        endpoint = self.endpoint

        if team_id:
            if isinstance(team_id, int):
                team_id = str(team_id)

            if isinstance(team_id, str):
                team_id = team_id.split(",")

            # Convert all int to string
            team_id = [str(x) for x in team_id if x] if team_id else None

            kwargs.update({"teamId": ",".join(team_id)})

        return super(API, self).get(endpoint=endpoint, **kwargs)

    def get_with_stats(self, team_id=None, **kwargs):
        if not team_id:
            raise ValueError("Team stats require a single Team ID.")

        try:
            team_id = int(team_id)
        except ValueError:
            raise ValueError("An invalid Team ID was passed into the team stats function.")

        kwargs.update({"expand": "team.stats"})
        return self.get(team_id=team_id, **kwargs)
