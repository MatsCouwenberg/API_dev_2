import requests

def test_get_teams():
    response = requests.get('https://f1-api-matscouwenberg.cloud.okteto.net/teams/')
    assert response.status_code == 200

    teams = response.json()
    for team in teams:
        assert type(team.get("name")) == str
        assert type(team.get("country")) == str
        assert type(team.get("id")) == int
