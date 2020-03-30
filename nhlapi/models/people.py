"""
We call this module People even though it returns a single Person Object to conform
to the NHL API naming conventions.
"""

from nhlapi.models.teams import Team


class Person(Model):
    _valid_properties = {
        "id": None,
        "fullName": None,
        "link": None,
        "firstName": None,
        "lastName": None,
        "primaryNumber": None,
        "birthDate": None,
        "currentAge": None,
        "birthCity": None,
        "birthStateProvince": None,
        "birthCountry": None,
        "nationality": None,
        "height": None,
        "weight": None,
        "active": None,
        "alternateCaptain": None,
        "captain": None,
        "rookie": None,
        "shootsCatches": None,
        "rosterStatus": None,
        "currentTeam": None,
        "primaryPosition": None,
    }

    def __init__(self, **kwargs):
        self.id = None
        self.fullName = None
        self.link = None
        self.firstName = None
        self.lastName = None
        self.primaryNumber = None
        self.birthDate = None
        self.currentAge = None
        self.birthCity = None
        self.birthStateProvince = None
        self.birthCountry = None
        self.nationality = None
        self.height = None
        self.weight = None
        self.active = None
        self.alternateCaptain = None
        self.captain = None
        self.rookie = None
        self.shootsCatches = None
        self.rosterStatus = None
        self.currentTeam = None
        self.primaryPosition: PersonPosition = None

        for key, default in Person._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        person = cls()
        # The people API only takes a single ID (this is always one player)
        single_person_json = json["people"][0]

        for key, val in single_person_json.items():
            if key == "currentTeam":
                setattr(person, key, Team.parse(val))
            elif key in cls._valid_properties:
                setattr(person, key, val)
        return person


class PersonPosition(Model):
    _valid_properties = {"code": None, "name": None, "type": None, "abbreviation": None}

    def __init__(self, **kwargs):
        self.code = None
        self.name = None
        self.type = None
        self.abbreviation = None

        for key, default in PersonPosition._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        position = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(position, key, val)
        return position
