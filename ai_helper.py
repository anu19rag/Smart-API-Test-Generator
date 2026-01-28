class AIHelper:

    @staticmethod
    def suggest_negative_cases(endpoint):
        return [
            {"invalid_token": True},
            {"empty_payload": True}
        ]
