from src.api import get_hand


def test_get_hand():
    response = get_hand()
    assert len(response["hand"]) == 2
    assert response["representation"]
