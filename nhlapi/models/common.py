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
                print(val)
                # Parse another level deeper
                for sub_k in val:
                    sub_v = getattr(self, sub_k)
                    if not Model._is_builtin(sub_v):
                        result[sub_k] = sub_v.as_dict()

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

            # Add it if it's not None
            if val:
                result[key] = val
        return result

    @classmethod
    def parse(cls, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError
