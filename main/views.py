from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from main.forms import GameModelForm
from main.models import Game, Species, Class, Skill, Talent


class IndexView(View):
    def get(self, request):
        return render(request, "base.html")


class GamesListView(ListView):
    model = Game
    template_name = 'list-view.html'


class GameCreateView(LoginRequiredMixin, CreateView):
    form_class = GameModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('games-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.success_url)

    def get_initial(self):
        game = get_object_or_404(Game, id=self.kwargs['pk'])
        initial_data = {
            'name': game.name,
            'description': game.description,
            'short_description': game.short_description,
            'rule_set': game.rule_set
        }
        return initial_data


class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('games-list')


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'form_confirm_delete.html'
    success_url = reverse_lazy('games-list')


class DashboardView(View):
    def get(self, request, pk):
        return render(request, 'dashboard.html')


class SpeciesListView(ListView):
    model = Species
    template_name = 'dashboard.html'


class ClassListView(ListView):
    model = Class
    template_name = 'dashboard.html'


class SkillListView(ListView):
    model = Skill
    template_name = 'dashboard.html'


class TalentListView(ListView):
    model = Talent
    template_name = 'dashboard.html'
