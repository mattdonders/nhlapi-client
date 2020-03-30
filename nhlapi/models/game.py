from enum import Enum

from nhlapi.models.teams import Team, Venue

from nhlapi.models.common import Model


class Game(Model):
    _valid_properties = {
        "gamePk": None,
        "link": None,
        "gameType": None,
        "season": None,
        "gameData": None,
        "status": None,
        "teams": {},
        "venue": None,
        "content": {},
    }

    def __init__(self, **kwargs):
        self.gamePk = None
        self.link = None
        self.gameType: GameType = None
        self.season = None
        self.gameData = None
        self.status = None
        self.teams: GameTeams = None
        self.venue = None
        self.content = None

        for key, default in Game._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        game = cls()
        # flat_json = flatten(json)
        for key, val in json.items():
            if key not in cls._valid_properties:
                continue

            if key == "status":
                setattr(game, key, GameStatus.parse(val))
            elif key == "venue":
                setattr(game, key, Venue.parse(val))
            elif key == "teams":
                setattr(game, key, GameTeams.parse(val))
            elif key == "gameType":
                setattr(game, key, GameType(val))
            elif key in cls._valid_properties:
                setattr(game, key, val)

        # Return the newly created & attributed Team object
        return game


class GameType(Enum):
    PRESEASON = "PR"
    REGULAR_SEASON = "R"
    PLAYOFFS = "P"
    ALL_STAR = "A"
    OLYMPIC = "O"
    EXHIBITION = "E"
    WORLD_CUP_OF_HOCKEY_EXHIBITION = "WCOH_EXH"
    WORLD_CUP_OF_HOCKEY_PRELIMINARY = "WCOH_PRELIM"
    WORLD_CUP_OF_HOCKEY_FINALS = "WCOH_FINAL"


class GameStatus(Model):
    _valid_properties = {
        "abstractGameState": None,
        "codedGameState": None,
        "detailedState": None,
        "statusCode": None,
        "startTimeTBD": False,
    }

    def __init__(self, **kwargs):
        self.abstractGameState = None
        self.codedGameState = None
        self.detailedState = None
        self.statusCode = None
        self.startTimeTBD = False

        for key, default in GameStatus._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        game_status = cls()
        # flat_json = flatten(json)
        for key, val in json.items():
            if key not in cls._valid_properties:
                continue

            if key in cls._valid_properties:
                setattr(game_status, key, val)

        # Return the newly created & attributed Team object
        return game_status


class GameTeams(Model):
    _valid_properties = {"away": None, "home": None}

    def __init__(self, **kwargs):
        self.away: Team = None
        self.home: Team = None

        for key, default in GameTeams._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        game_teams = cls()
        # flat_json = flatten(json)
        for key, val in json.items():
            if key not in cls._valid_properties:
                continue

            if key in cls._valid_properties:
                setattr(game_teams, key, Team.parse(val))

        # Return the newly created & attributed Team object
        return game_teams
