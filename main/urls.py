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

from main import views


urlpatterns = [
    # authentication required views
    path('game/edit/<int:pk>', views.GameUpdateView.as_view(), name='game-update'),
    path('game/create/<int:pk>', views.GameCreateView.as_view(), name='game-create'),
    path('game/delete/<int:pk>', views.GameDeleteView.as_view(), name='game-delete'),
    path('game/details/<int:pk>', views.GameDetailView.as_view(), name='game-details'),

    path('user/<int:pk>/dashboard', views.DashboardView.as_view(), name='dashboard'),

    path('species-list/', views.SpeciesListView.as_view(), name='species-list'),
    path('class-list/', views.ClassListView.as_view(), name='class-list'),
    path('career-list/', views.CareerListView.as_view(), name='career-list'),
    path('skill-list/', views.SkillListView.as_view(), name='skill-list'),
    path('talent-list/', views.TalentListView.as_view(), name='talent-list'),

    path('species/edit/<int:pk>', views.SpeciesUpdateView.as_view(), name='species-update'),
    path('species/create/<int:pk>', views.SpeciesCreateView.as_view(), name='species-create'),
    path('species/delete/<int:pk>', views.SpeciesDeleteView.as_view(), name='species-delete'),
    path('species/details/<int:pk>', views.SpeciesDetailView.as_view(), name='species-details'),

    path('class/edit/<int:pk>', views.ClassUpdateView.as_view(), name='class-update'),
    path('class/create/<int:pk>', views.ClassCreateView.as_view(), name='class-create'),
    path('class/delete/<int:pk>', views.ClassDeleteView.as_view(), name='class-delete'),
    path('class/details/<int:pk>', views.ClassDetailView.as_view(), name='class-details'),

    path('career/edit/<int:pk>', views.CareerUpdateView.as_view(), name='career-update'),
    path('career/create/<int:pk>', views.CareerCreateView.as_view(), name='career-create'),
    path('career/delete/<int:pk>', views.CareerDeleteView.as_view(), name='career-delete'),
    path('career/details/<int:pk>', views.CareerDetailView.as_view(), name='career-details'),

    path('skill/edit/<int:pk>', views.SkillUpdateView.as_view(), name='skill-update'),
    path('skill/create/<int:pk>', views.SkillCreateView.as_view(), name='skill-create'),
    path('skill/delete/<int:pk>', views.SkillDeleteView.as_view(), name='skill-delete'),
    path('skill/details/<int:pk>', views.SkillDetailView.as_view(), name='skill-details'),

    path('talent/edit/<int:pk>', views.TalentUpdateView.as_view(), name='talent-update'),
    path('talent/create/<int:pk>', views.TalentCreateView.as_view(), name='talent-create'),
    path('talent/delete/<int:pk>', views.TalentDeleteView.as_view(), name='talent-delete'),
    path('talent/details/<int:pk>', views.TalentDetailView.as_view(), name='talent-details'),
]
