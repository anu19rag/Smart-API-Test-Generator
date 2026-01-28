from core.test_generator import TestGenerator
import os


def main():
    generator = TestGenerator("swagger/openapi.json")
    generator.generate_tests()

    os.system("pytest tests/ --alluredir=reports")


if __name__ == "__main__":
    main()
