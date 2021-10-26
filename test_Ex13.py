import pytest
import requests

class TestGetUserAgent:
    data = [
        (
            "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mobile",
            "No",
            "Android"
        ),
        (
            "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "Mobile",
            "Chrome",
            "iOS"
        ),
        (
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Googlebot",
            "Unknown",
            "Unknown"
        ),
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "Web",
            "Chrome",
            "No"
        ),
        (
            "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "Mobile",
            "No",
            "iPhone"
        )
    ]
    @pytest.mark.parametrize('agent, platform, browser, device', data)
    def test_get_user_agent(self, agent, platform, browser, device):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data2 = {"user-agent": agent}

        response = requests.get(url, headers=data2)
        parsed_response = response.json()

        for param in parsed_response:
            if param == "platform":
                if parsed_response[param] != platform:
                    print(f" {agent} contains {param} parameter with {parsed_response[param]} value")
            if param == "browser":
                if parsed_response[param] != browser:
                    print(f" {agent} contains {param} parameter with {parsed_response[param]} value")
            if param == "device":
                if parsed_response[param] != device:
                    print(f" {agent} contains {param} parameter with {parsed_response[param]} value")
