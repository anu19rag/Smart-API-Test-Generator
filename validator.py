from jsonschema import validate


class Validator:

    @staticmethod
    def validate_status_code(response, expected=200):
        assert response.status_code == expected

    @staticmethod
    def validate_schema(response, schema):
        validate(instance=response.json(), schema=schema)
