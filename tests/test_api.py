import requests


def test_get_hand():
    response = requests.get("http://localhost:8000/v1/hand")
    assert response.ok
