import pytest
from rblx import get_username, greet

def test_get_username():
    assert get_username(123) == "User_123"

def test_greet():
    assert greet("TuFueguito") == "Hello, TuFueguito! Welcome to RBLX."
