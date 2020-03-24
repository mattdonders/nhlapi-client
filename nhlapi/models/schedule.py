from nhlapi.models.teams import Team, Venue
from nhlapi.models.game import Game, GameTeams


class Schedule:
    _valid_properties = {"totalItems": None, "totalEvents": None, "totalGames": None, "totalMatches": None, "dates": []}

    def __init__(self, **kwargs):
        for key, default in Schedule._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        schedule = cls()
        # flat_json = flatten(json)
        for key, val in json.items():
            if key not in cls._valid_properties:
                continue

            if key == "dates":
                dates = [ScheduleDate.parse(date) for date in val]
                setattr(schedule, key, dates)
            elif key in cls._valid_properties:
                setattr(schedule, key, val)

        # Return the newly created & attributed Team object
        return schedule


class ScheduleDate:
    _valid_properties = {
        "date": None,
        "totalItems": None,
        "totalEvents": None,
        "totalGames": None,
        "totalMatches": None,
        "games": [],
    }

    def __init__(self, **kwargs):
        for key, default in ScheduleDate._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        schedule_date = cls()
        # flat_json = flatten(json)
        for key, val in json.items():
            if key not in cls._valid_properties:
                continue

            if key == "games":
                games = [Game.parse(game) for game in val]
                setattr(schedule_date, key, games)
            elif key in cls._valid_properties:
                setattr(schedule_date, key, val)

        # Return the newly created & attributed Team object
        return schedule_date
