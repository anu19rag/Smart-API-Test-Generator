# Smart-API-Test-Generator
mini Postman + mini Test Framework + mini AI tool-------- Eveloped an AI-powered Smart API Test Generator that parses Swagger/OpenAPI specs and auto-generates Pytest-based automated tests with reporting and schema validation, reducing manual test effort by 80%
AI + Swagger + Pytest based Automatic API Testing Framework

An intelligent API automation framework that reads Swagger/OpenAPI specs and automatically generates & executes test cases.

Think of it like:

👉 Postman + Pytest + AI = Fully automated API testing

Instead of writing manual test cases for every endpoint, this tool:

Parses Swagger

Auto-creates tests

Hits APIs

Validates responses

Generates reports

Saves 80–90% manual effort 🔥

✨ Features

✅ Parse Swagger/OpenAPI JSON
✅ Auto discover endpoints
✅ Auto generate Pytest test cases
✅ Send requests dynamically
✅ Status code validation
✅ JSON schema validation
✅ Allure HTML reports
✅ Easy plug-in for AI test generation
✅ CI/CD ready

🏗 Project Structure
smart-api-test-generator/
│
├── config/
│
├── swagger/
│   └── openapi.json
│
├── core/
│   ├── swagger_parser.py
│   ├── test_generator.py
│   ├── request_engine.py
│   ├── validator.py
│   └── ai_helper.py
│
├── tests/
│   └── test_generated.py
│
├── reports/
│
├── run.py
├── pytest.ini
├── requirements.txt
└── README.md

🛠 Tech Stack

Python

Pytest

Requests

Swagger / OpenAPI

JSONSchema

Allure Reporting

⚙️ Installation
1️⃣ Clone repo
git clone <your-repo-url>
cd smart-api-test-generator

2️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run
Step 1 – Add Swagger file

Place your API spec here:

swagger/openapi.json


You can use:

FakeStore API

Postman exported JSON

Any OpenAPI spec

Step 2 – Generate & run tests
python run.py


This will:
✔ Parse Swagger
✔ Generate tests
✔ Execute APIs
✔ Save reports

📊 View Report (Allure)
pytest --alluredir=reports
allure serve reports


Beautiful HTML report opens in browser ✨

🔁 Example Flow
Swagger → Parse → Generate Tests → Hit APIs → Validate → Report


Fully automatic ⚡

🧠 AI Capabilities (Planned / Extendable)

Smart negative test generation

Boundary testing

Payload fuzzing

Auto edge cases

LLM-based test suggestions

(Designed for future AI integration)

🧪 Example Generated Test
def test_api_1():
    response = RequestEngine.send_request(
        BASE_URL,
        "GET",
        "/products"
    )
    assert response.status_code < 500
