import requests


class RequestEngine:

    @staticmethod
    def send_request(base_url, method, endpoint, payload=None, headers=None):
        url = base_url + endpoint

        response = requests.request(
            method=method,
            url=url,
            json=payload,
            headers=headers
        )

        return response
