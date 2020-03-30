import requests
from .models import Teams


class NHLAPI(Model):
    NHL_API_BASE_URL = "https://statsapi.web.nhl.com/api/v1"

    @classmethod
    def __nhl_client(cls, url, query_args=None):
        """ This method makes the actual call to the NHL API. """
        try:
            response = requests.get(url, params=query_args)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Uncaught Exception:", err)

        return response.json()

    @classmethod
    def get_teams(cls, team_id=None, **kwargs):
        print(team_id, kwargs)
        teams_url = f"{cls.NHL_API_BASE_URL}/teams/{team_id or ''}"
        print(teams_url)
        response = cls.__nhl_client(teams_url, kwargs)
        return response


if __name__ == "__main__":
    nhlapi = NHLAPI()
    print(nhlapi.get_teams())
    print("#" * 50)
    print(nhlapi.get_teams(team_id=1))
    print("#" * 50)
    print(nhlapi.get_teams(team_id=1, expand="team.roster"))
