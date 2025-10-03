import ast
import builtins


class Parameter:
    def __init__(self, name: str, value: str, parameter_type: str):
        self.name = name
        self.value = value
        self.parameter_type = parameter_type

    def to_json(self):
        return {
            "name": self.name,
            "value": str(self.value),
            "parameter_type": self.parameter_type,
        }

    @staticmethod
    def _convert_type(stringed_value: str, parameter_type: str):
        converted_value = ast.literal_eval(stringed_value)
        target_type = getattr(builtins, parameter_type)
        if not isinstance(converted_value, target_type):
            raise ValueError(
                f"Type inference went wrong: expected type {target_type} but got {type(converted_value)}"
            )
        return converted_value

    @classmethod
    def from_json(cls, json_data):
        converted_value = cls._convert_type(
            json_data["value"], json_data["parameter_type"]
        )
        return cls(json_data["name"], converted_value, json_data["parameter_type"])
