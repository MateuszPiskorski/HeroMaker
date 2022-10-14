import pytest
from django.contrib.auth.models import User

from main.models import Game


@pytest.fixture
def user():
    return User.objects.create(username="test")


@pytest.fixture
def games():
    lst = []
    for x in range(10):
        lst.append(Game.objects.create(name=x, description=x, short_description=x))
    return lst
