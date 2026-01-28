from core.swagger_parser import SwaggerParser


class TestGenerator:

    def __init__(self, swagger_path):
        self.parser = SwaggerParser(swagger_path)

    def generate_tests(self, output_file="tests/test_generated.py"):
        endpoints = self.parser.get_endpoints()

        with open(output_file, "w") as f:
            f.write("import pytest\n")
            f.write("from core.request_engine import RequestEngine\n\n")

            f.write("BASE_URL = 'https://fakestoreapi.com'\n\n")

            for i, ep in enumerate(endpoints):
                test_name = f"test_api_{i}"

                f.write(f"""
def {test_name}():
    response = RequestEngine.send_request(
        BASE_URL,
        "{ep['method']}",
        "{ep['path']}"
    )
    assert response.status_code < 500
""")
