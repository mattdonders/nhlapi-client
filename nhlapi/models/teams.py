from typing import List

from nhlapi.models.common import Model

# This old method stores all the Teams at the Teams.teams attribute.
# The one below this will store Teams as a list of Teams instead.
# class Teams(Model):
#     _valid_properties = {"teams": []}

#     def __init__(self, **kwargs):
#         for key, default in Teams._valid_properties.items():
#             setattr(self, key, kwargs.get(key, default))

#     @classmethod
#     def parse(cls, json):
#         teams = cls()
#         for key, val in json.items():
#             if key == "teams":
#                 list_of_teams = [Team.parse(team) for team in val]
#                 setattr(teams, key, list_of_teams)
#             elif key in cls._valid_properties:
#                 setattr(teams, key, val)
#         return teams


class Teams(Model):
    _valid_properties = {"teams": []}

    def __init__(self, **kwargs):
        self.teams: List[Team] = []

        for key, default in Teams._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        teams = cls()
        for key, val in json.items():
            if key == "teams":
                list_of_teams = [Team.parse(team) for team in val]
                setattr(teams, key, list_of_teams)
            elif key in cls._valid_properties:
                setattr(teams, key, val)
        return teams


class Team(Model):
    _valid_properties = {
        "id": None,
        "name": None,
        "link": None,
        "venue": None,
        "abbreviation": None,
        "teamName": None,
        "locationName": None,
        "division": None,
        "conference": None,
        "franchise": None,
        "previousGameSchedule": {},
        "shortName": None,
        "leagueRecord": None,
        "teamStats": None,
    }

    def __init__(self, **kwargs):
        self.id = None
        self.name = None
        self.link = None
        self.venue: Venue = None
        self.abbreviation = None
        self.teamName = None
        self.locationName = None
        self.division: Division = None
        self.conference: Conference = None
        self.franchise: Franchise = None
        self.previousGameSchedule = {}
        self.shortName = None
        self.leagueRecord: LeagueRecord = None
        self.teamStats = None

        for key, default in Team._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        team = cls()
        # flat_json = flatten(json)
        for key, val in json.items():
            if key not in cls._valid_properties:
                continue

            # Always run the regular setattr regardless of type
            # setattr(team, key, val)
            if key == "division":
                setattr(team, key, Division.parse(val))
            elif key == "conference":
                setattr(team, key, Conference.parse(val))
            elif key == "franchise":
                setattr(team, key, Franchise.parse(val))
            elif key == "venue":
                setattr(team, key, Venue.parse(val))
            elif key == "leagueRecord":
                setattr(team, key, LeagueRecord.parse(val))
            elif key in cls._valid_properties:
                setattr(team, key, val)

        # Return the newly created & attributed Team object
        return team


class Conference(Model):
    _valid_properties = {"id": None, "name": None, "link": None}

    def __init__(self, **kwargs):
        self.id = None
        self.name = None
        self.link = None

        for key, default in Conference._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        conference = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(conference, key, val)

        return conference


class Division(Model):
    """
    Describes a Team's Division object.

    Args:
        **kwargs: Variables defined in JSON payload from NHL API.

    Attributes:
        id (str): The Division ID
        name (str): The Division name
        nameShort (str): The short Division name
        link (str): The link to the Division's API endpoint.
        abbreviation (str): The Division abbreviation.
    """

    _valid_properties = {"id": None, "name": None, "nameShort": None, "link": None, "abbreviation": None}

    def __init__(self, **kwargs):
        self.id = None
        self.name = None
        self.nameShort = None
        self.link = None
        self.abbreviation = None

        for key, default in Division._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        division = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(division, key, val)

        return division


class Franchise(Model):
    _valid_properties = {"franchiseId": None, "teamName": None, "link": None}

    def __init__(self, **kwargs):
        for key, default in Franchise._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        franchise = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(franchise, key, val)
        return franchise


class LeagueRecord(Model):
    _valid_properties = {"wins": None, "losses": None, "ot": None, "type": None}

    def __init__(self, **kwargs):
        self.wins = None
        self.losses = None
        self.ot = None
        self.type = None

        for key, default in LeagueRecord._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        league_record = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(league_record, key, val)
        return league_record

    @property
    def formatted(self):
        return f"{self.wins}-{self.losses}-{self.ot}"


class Venue(Model):
    _valid_properties = {"name": None, "link": None, "city": None, "timeZone": None}

    def __init__(self, **kwargs):
        self.name = None
        self.link = None
        self.city = None
        self.timeZone: VenueTimeZone = None

        for key, default in Venue._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        venue = cls()
        for key, val in json.items():
            if key == "timeZone":
                setattr(venue, key, VenueTimeZone.parse(val))
            elif key in cls._valid_properties:
                setattr(venue, key, val)
        return venue


class VenueTimeZone(Model):
    _valid_properties = {"id": None, "offset": None, "tz": None}

    def __init__(self, **kwargs):
        for key, default in VenueTimeZone._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        venue_timezone = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(venue_timezone, key, val)
        return venue_timezone
