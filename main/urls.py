"""HeroMaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main.views import (
    GameUpdateView,
    GameCreateView,
    GameDeleteView,
    DashboardView,
    SpeciesListView,
    ClassListView,
    SkillListView,
    TalentListView,
)

urlpatterns = [
    # authentication not required views
    path('game/edit/<int:pk>', GameUpdateView.as_view(), name='game-update'),
    path('game/create/<int:pk>', GameCreateView.as_view(), name='game-create'),
    path('game/delete/<int:pk>', GameDeleteView.as_view(), name='game-delete'),

    # authentication required views
    path('user/<int:pk>/dashboard', DashboardView.as_view(), name='dashboard'),
    path('species-list/', SpeciesListView.as_view(), name='species-list'),
    path('class-list/', ClassListView.as_view(), name='class-list'),
    path('skill-list/', SkillListView.as_view(), name='skill-list'),
    path('talent-list/', TalentListView.as_view(), name='talent-list'),
]
