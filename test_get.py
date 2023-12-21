import requests

def test_get_drivers():
    response = requests.get('https://f1-api-matscouwenberg.cloud.okteto.net/drivers/')
    assert response.status_code == 200

    drivers = response.json()
    for driver in drivers:
        assert type(driver.get("number")) == int
        assert type(driver.get("name")) == str
        assert type(driver.get("nationality")) == str
        assert type(driver.get("id")) == int


def test_get_circuits():
    response = requests.get('https://f1-api-matscouwenberg.cloud.okteto.net/circuits/')
    assert response.status_code == 200

    circuits = response.json()
    for circuit in circuits:
        assert type(circuit.get("name")) == str
        assert type(circuit.get("country")) == str
        assert type(circuit.get("id")) == int


def test_get_teams():
    response = requests.get('https://f1-api-matscouwenberg.cloud.okteto.net/teams/')
    assert response.status_code == 200

    teams = response.json()
    for team in teams:
        assert type(team.get("name")) == str
        assert type(team.get("country")) == str
        assert type(team.get("id")) == int