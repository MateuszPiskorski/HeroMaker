from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, FormView, DeleteView

from main.forms import GameModelForm
from main.models import Game


class IndexView(View):
    def get(self, request):
        return render(request, "base.html")


class GamesListView(ListView):
    model = Game
    template_name = 'list-view.html'


class GameCreateView(LoginRequiredMixin, FormView):
    model = Game
    form_class = GameModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('games-list')


class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('games-list')

    def get_initial(self):
        user = User.objects.filter(pk=self.request.user.id)
        return {'author': user}


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'form_confirm_delete.html'
    success_url = reverse_lazy('games-list')
