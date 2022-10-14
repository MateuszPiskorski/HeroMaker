import pytest
from django.urls import reverse


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
