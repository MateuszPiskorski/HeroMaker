import pytest
from django.urls import reverse

from main.forms import GameModelForm, SpeciesModelForm, ClassModelForm, SkillModelForm, TalentModelForm
from main.models import Game, Species, Class, Career, Skill, Talent


@pytest.mark.django_db
def test_check_settings():
    assert True


def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_game_list_view(client, games):
    url = reverse('games-list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(games)
    for game in games:
        assert game in response.context['object_list']


@pytest.mark.django_db
def test_species_list_view_login(client, species):
    url = reverse('species-list')
    logged_user = species[0].author
    client.force_login(logged_user)
    client_species = [speciee for speciee in species if speciee.author == logged_user]
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(client_species)
    # for specie in species:
    #     assert specie in response.context['object_list']


def test_species_list_view_not_login(client):
    url = reverse('species-list')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


@pytest.mark.django_db
def test_class_list_view_login(client, classes):
    url = reverse('class-list')
    logged_user = classes[0].author
    client.force_login(logged_user)
    client_classes = [class_ for class_ in classes if class_.author == logged_user]
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(client_classes)
    # for class_ in classes:
    #     assert class_ in response.context['object_list']


def test_class_list_view_not_login(client):
    url = reverse('class-list')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


@pytest.mark.django_db
def test_career_list_view_login(client, careers):
    url = reverse('career-list')
    logged_user = careers[0].author
    client.force_login(logged_user)
    client_careers = [career for career in careers if career.author == logged_user]
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(client_careers)
    # for career in careers:
    #     assert career in response.context['object_list']


def test_career_list_view_not_login(client):
    url = reverse('career-list')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


@pytest.mark.django_db
def test_skill_list_view_login(client, skills):
    url = reverse('skill-list')
    logged_user = skills[0].author
    client.force_login(logged_user)
    client_skills = [skill for skill in skills if skill.author == logged_user]
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(client_skills)
    # for skill in skills:
    #     assert skill in response.context['object_list']


def test_skill_list_view_not_login(client):
    url = reverse('skill-list')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


@pytest.mark.django_db
def test_talent_list_view_login(client, talents):
    url = reverse('talent-list')
    logged_user = talents[0].author
    client.force_login(logged_user)
    client_talent = [talent for talent in talents if talent.author == logged_user]
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(client_talent)
    # for talent in talents:
    #     assert talent in response.context['object_list']


def test_talent_list_view_not_login(client):
    url = reverse('talent-list')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


@pytest.mark.django_db
def test_game_create_get_login(client, user, games):
    game = games[0]
    url = reverse('game-create', args=(game.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_game_create_get_not_login(client, user, games):
    game = games[0]
    url = reverse('game-create', args=(game.id,))
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


@pytest.mark.django_db
def test_game_create_post_login(client, user, games):
    game = games[0]
    url = reverse('game-create', args=(game.id,))
    client.force_login(user)
    data = {
        'name': 'newname',
        'description': 'newdesc',
        'rule_set': 'whatever',
        'short_description': 'newshortdesc',
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('games-list')
    assert response.url.startswith(url_redirect)
    Game.objects.get(**data)


@pytest.mark.django_db
def test_game_update_get_login_user(client, user, games):
    game = games[0]
    url = reverse('game-update', args=(game.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_game_update_get_not_login(client, user, games):
    game = games[0]
    url = reverse('game-update', args=(game.id,))
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


@pytest.mark.django_db
def test_game_update_get_login_superuser(client, superuser, games):
    game = games[0]
    url = reverse('game-update', args=(game.id,))
    client.force_login(superuser)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, GameModelForm)


@pytest.mark.django_db
def test_game_update_post_login_superuser(client, superuser, games):
    game = games[0]
    url = reverse('game-update', args=(game.id,))
    client.force_login(superuser)
    data = {
        'name': 'whatever',
        'description': 'whatever',
        'rule_set': 'whatever',
        'short_description': 'whatever',
        'author': superuser.id,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('games-list')
    assert response.url.startswith(url_redirect)
    Game.objects.get(name=data['name'])


@pytest.mark.django_db
def test_game_delete_get_login_user(client, user, games):
    game = games[0]
    url = reverse('game-delete', args=(game.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_game_delete_get_not_login(client, user, games):
    game = games[0]
    url = reverse('game-delete', args=(game.id,))
    response = client.get(url)
    assert response.status_code == 302
    url_redirect = reverse('login')
    assert response.url.startswith(url_redirect)


# @pytest.mark.django_db
# def test_game_delete_post_login_superuser(client, superuser, games):
#     game = games[0]
#     url = reverse('game-delete', args=(game.id,))
#     client.force_login(superuser)
#     response = client.post(url)
#     assert response.status_code == 302


@pytest.mark.django_db
def test_species_create_get_login(client, user, species):
    speciee = species[0]
    url = reverse('species-create', args=(speciee.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_species_create_post_login(client, user, species):
    speciee = species[0]
    url = reverse('species-create', args=(speciee.id,))
    client.force_login(user)
    data = {
        'name': 'newname',
        'description': 'newdesc',
        'short_description': 'newshortdesc',
        'disallowed_careers': [1, 2],
        'skills': [1, 2, 3],
        'talents': [3, 4],
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('species-list')
    assert response.url.startswith(url_redirect)
    Species.objects.get(**data)


@pytest.mark.django_db
def test_species_update_get_login(client, user, species):
    speciee = species[0]
    url = reverse('species-update', args=(speciee.id,))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, SpeciesModelForm)


@pytest.mark.django_db
def test_species_update_post_login(client, user, species):
    speciee = species[0]
    url = reverse('species-create', args=(speciee.id,))
    client.force_login(user)
    data = {
        'name': 'newname',
        'description': 'newdesc',
        'short_description': 'newshortdesc',
        'disallowed_careers': [1, 2],
        'skills': [1, 2, 3],
        'talents': [3, 4],
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('species-list')
    assert response.url.startswith(url_redirect)
    Species.objects.get(name=data['newname'])


@pytest.mark.django_db
def test_class_create_get_login(client, user, classes):
    _class = classes[0]
    url = reverse('class-create', args=(_class.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_class_create_post_login(client, user, classes):
    _class = classes[0]
    url = reverse('class-create', args=(_class.id,))
    client.force_login(user)
    data = {
        'name': 'whatever',
        'description': 'whatever',
        'short_description': 'whatever',
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('class-list')
    assert response.url.startswith(url_redirect)
    Class.objects.get(**data)


@pytest.mark.django_db
def test_class_update_get_login(client, user, classes):
    _class = classes[0]
    url = reverse('class-update', args=(_class.id,))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, ClassModelForm)


@pytest.mark.django_db
def test_class_update_post_login(client, user, classes):
    _class = classes[0]
    url = reverse('class-update', args=(_class.id,))
    client.force_login(user)
    data = {
        'name': 'newname',
        'description': 'newdesc',
        'short_description': 'newshortdesc',
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('class-list')
    assert response.url.startswith(url_redirect)
    Class.objects.get(name=data['name'])


@pytest.mark.django_db
def test_career_create_get_login(client, user, careers):
    career = careers[0]
    url = reverse('career-create', args=(career.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_career_create_post_login(client, user, careers, classes, talents, skills):
    career = careers[0]
    _class = classes[0]
    url = reverse('career-create', args=(career.id,))
    client.force_login(user)
    data = {
        'name': 'whatever',
        'description': 'whatever',
        'short_description': 'whatever',
        'first_level_name': 'whatever',
        '_class': _class,
        'talents': [1, 2],
        'skills': [1, 2],
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('career-list')
    assert response.url.startswith(url_redirect)
    Career.objects.get(**data)


@pytest.mark.django_db
def test_career_update_get_login(client, user, careers):
    career = careers[0]
    url = reverse('career-update', args=(career.id,))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, ClassModelForm)


@pytest.mark.django_db
def test_career_update_post_login(client, user, careers, classes, talents, skills):
    career = careers[0]
    _class = classes[0]
    url = reverse('career-update', args=(career.id,))
    client.force_login(user)
    data = {
        'name': 'new',
        'description': 'new',
        'short_description': 'new',
        'first_level_name': 'new',
        '_class': _class,
        'talents': [1, 2],
        'skills': [1, 2],
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('career-list')
    assert response.url.startswith(url_redirect)
    Career.objects.get(name=data['name'])


@pytest.mark.django_db
def test_skill_create_get_login(client, user, skills):
    skill = skills[0]
    url = reverse('skill-create', args=(skill.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_skill_create_post_login(client, user, skills):
    skill = skills[0]
    url = reverse('skill-create', args=(skill.id,))
    client.force_login(user)
    data = {
        'name': 'whatever',
        'description': 'whatever',
        'short_description': 'whatever',
        'characteristic': 'whatever',
        'is_advanced': False,
        'is_grouped': False,
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('skill-list')
    assert response.url.startswith(url_redirect)
    Skill.objects.get(**data)


@pytest.mark.django_db
def test_skill_update_get_login(client, user, skills):
    skill = skills[0]
    url = reverse('skill-update', args=(skill.id,))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, SkillModelForm)


@pytest.mark.django_db
def test_skill_update_post_login(client, user, skills):
    skill = skills[0]
    url = reverse('skill-update', args=(skill.id,))
    client.force_login(user)
    data = {
        'name': 'new',
        'description': 'new',
        'short_description': 'new',
        'characteristic': 'new',
        'is_advanced': True,
        'is_grouped': True,
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('skill-list')
    assert response.url.startswith(url_redirect)
    Skill.objects.get(name=data['name'])


@pytest.mark.django_db
def test_talent_create_get_login(client, user, talents):
    talent = talents[0]
    url = reverse('talent-create', args=(talent.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_talent_create_post_login(client, user, talents):
    talent = talents[0]
    url = reverse('talent-create', args=(talent.id,))
    client.force_login(user)
    data = {
        'name': 'whatever',
        'tests': 'whatever',
        'description': 'whatever',
        'bonus_when_maxed': 'whatever',
        'short_description': "whatever",
        'level': 1,
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('talent-list')
    assert response.url.startswith(url_redirect)
    Talent.objects.get(**data)


@pytest.mark.django_db
def test_talent_update_get_login(client, user, talents):
    talent = talents[0]
    url = reverse('talent-update', args=(talent.id,))
    client.force_login(user)
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, TalentModelForm)


@pytest.mark.django_db
def test_talent_update_post_login(client, user, talents):
    talent = talents[0]
    url = reverse('talent-update', args=(talent.id,))
    client.force_login(user)
    data = {
        'name': 'new',
        'tests': 'new',
        'description': 'new',
        'bonus_when_maxed': 'new',
        'short_description': 'new',
        'level': 1,
        'author': user,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    url_redirect = reverse('talent-list')
    assert response.url.startswith(url_redirect)
    Talent.objects.get(name=data['name'])
