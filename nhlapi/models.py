from datetime import datetime

import json as _json


class Model:
    def __init__(self):
        self._valid_properties = {}

    @classmethod
    def _is_builtin(cls, obj):
        return isinstance(obj, (int, float, str, list, dict, bool))

    def as_dict(self):
        """ Returns a dict representation of the resource """
        result = {}
        for key in self._valid_properties:
            val = getattr(self, key)
            if isinstance(val, datetime):
                val = val.isoformat()
            # Parse custom classes
            elif val and not Model._is_builtin(val):
                val = val.as_dict()
            # Parse lists of objects
            elif isinstance(val, list):
                # We only want to call as_dict in the case where the item
                # isn't a builtin type.
                for i in range(len(val)):
                    if Model._is_builtin(val[i]):
                        continue
                    val[i] = val[i].as_dict()
            # If it's a boolean, add it regardless of the value
            elif isinstance(val, bool):
                result[key] = val
            # If its a dictionary, parse two levels deeper
            elif isinstance(val, dict):
                for k, v in val.items():
                    if isinstance(v, dict):
                        for sub_k, sub_v in val.items():
                            new_key = f"{key}_{k}_{sub_k}"
                            print(new_key)
                            result[new_key] = sub_v
                    else:
                        new_key = f"{key}_{k}"
                        result[new_key] = v

            # Add it if it's not None
            if val:
                result[key] = val
        return result

    @classmethod
    def parse(cls, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError


class Teams(Model):
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


class Team(Model):
    _valid_properties = {
        "id": None,
        "name": None,
        "venue": {},
        "abbreviation": None,
        "teamName": None,
        "locationName": None,
        "division": {},
        "conference": {},
        "franchise": {},
        "shortName": None,
    }

    def __init__(self, **kwargs):
        for key, default in Team._valid_properties.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def parse(cls, json):
        team = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(team, key, val)
        return team
