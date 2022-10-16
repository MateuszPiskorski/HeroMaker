import pytest
from django.contrib.auth.models import User

from main.models import Game, Species, Class, Career, Skill, Talent


@pytest.fixture
def user():
    return User.objects.create(username="test")


@pytest.fixture
def superuser():
    return User.objects.create(username="test", is_superuser=True)


@pytest.fixture
def authors():
    lst = []
    for x in range(10):
        lst.append(User.objects.create(username=x))
    return lst


@pytest.fixture
def games(authors):
    lst = []
    for author in authors:
        lst.append(
            Game.objects.create(
                name="some game",
                description="some desc",
                short_description="short desc",
                author=author,
            )
        )
    return lst


@pytest.fixture
def classes(authors):
    lst = []
    for author in authors:
        lst.append(
            Class.objects.create(
                name="class",
                description="some desc",
                short_description="short desc",
                author=author
            )
        )
    return lst


@pytest.fixture
def skills(authors):
    lst = []
    for author in authors:
        lst.append(
            Skill.objects.create(
                name="species",
                characteristic="char",
                description="some desc",
                short_description="short desc",
                is_advanced=False,
                is_grouped=False,
                author=author
            )
        )
    return lst


@pytest.fixture
def talents(authors):
    lst = []
    for author in authors:
        lst.append(
            Talent.objects.create(
                name="talent",
                tests="tests",
                description="desc",
                bonus_when_maxed="bonus",
                short_description="short desc",
                level=1,
                author=author
            )
        )
    return lst


@pytest.fixture
def careers(authors, classes, talents, skills):
    lst = []
    for author, class_, talent, skill in zip(authors, classes, talents, skills):
        lst.append(
            Career.objects.create(
                name="species",
                description="some desc",
                short_description="short desc",
                first_level_name="level",
                talents=talent,
                skills=skill,
                _class=class_,
                author=author,
            )
        )
    return lst


@pytest.fixture
def species(authors, careers, talents, skills):
    lst = []
    for author, career, talent, skill in zip(authors, careers, talents, skills):
        lst.append(
            Species.objects.create(
                name="species",
                description="some desc",
                short_description="short desc",
                disallowed_careers=career,
                skills=skill,
                talents=talent,
                author=author
            )
        )
    return lst
