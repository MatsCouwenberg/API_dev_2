import requests

def test_get_drivers():
    response = requests.get('http://127.0.0.1:8000/drivers/')
    assert response.status_code == 200

    drivers = response.json()
    for driver in drivers:
        assert type(driver.get("number")) == int
        assert type(driver.get("name")) == str
        assert type(driver.get("nationality")) == str
        assert type(driver.get("id")) == int