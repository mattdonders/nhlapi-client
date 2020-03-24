class Teams:
    _valid_properties = {"teams": []}

    def __init__(self, **kwargs):
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


class Team:
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
            elif key in cls._valid_properties:
                setattr(team, key, val)

        # Return the newly created & attributed Team object
        return team


class Conference:
    _valid_properties = {"id": None, "name": None, "link": None}

    def __init__(self, **kwargs):
        for key, default in Conference._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        conference = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(conference, key, val)

        return conference


class Division:
    _valid_properties = {"id": None, "name": None, "nameShort": None, "link": None, "abbreviation": None}

    def __init__(self, **kwargs):
        for key, default in Division._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        division = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(division, key, val)

        return division


class Franchise:
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


class LeagueRecord:
    _valid_properties = {"wins": None, "losses": None, "ot": None, "type": None}

    def __init__(self, **kwargs):
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


class Venue:
    _valid_properties = {"name": None, "link": None, "city": None, "timeZone": None}

    def __init__(self, **kwargs):
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


class VenueTimeZone:
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
