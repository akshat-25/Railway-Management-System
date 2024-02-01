import pytest


def test_login_user(mock_get_user_from_db):
    mock_get_user_from_db.return_value = {"username": "tester123", "password": ""}
