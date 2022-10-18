from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.db.models import Q

from main.forms import GameModelForm, SpeciesModelForm, ClassModelForm, SkillModelForm, TalentModelForm, CareerModelForm
from main.models import Game, Species, Class, Skill, Talent, Career


class IndexView(View):
    def get(self, request):
        return render(request, "base.html")


class GamesListView(ListView):
    model = Game
    template_name = 'list-view.html'
    paginate_by = 15


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


class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    form_class = GameModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('games-list')

    def test_func(self):
        user = self.request.user
        if user.is_superuser:
            return True
        else:
            print("You need to be a superuser to preform this operation")
            return False


class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    template_name = 'form_confirm_delete.html'

    login_url = 'login'
    success_url = reverse_lazy('games-list')

    def test_func(self):
        user = self.request.user
        if user.is_superuser:
            return True
        else:
            print("You need to be a superuser to preform this operation")
            return False


class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'game-detail-view.html'
    context_object_name = 'game'

    login_url = 'login'


class DashboardView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk):
        return render(request, 'dashboard.html')


class SpeciesListView(LoginRequiredMixin, ListView):
    model = Species
    template_name = 'dashboard.html'
    paginate_by = 15

    login_url = 'login'

    def get_queryset(self):
        return Species.objects.filter(Q(author__isnull=True) | Q(author=self.request.user)).order_by('name')


class SpeciesCreateView(LoginRequiredMixin, CreateView):
    model = Species
    form_class = SpeciesModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('species-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.success_url)

    # def get_initial(self):
    #     species = get_object_or_404(Species, id=self.kwargs['pk'])
    #     initial_data = {
    #         'name': species.name,
    #         'description': species.description,
    #         'short_description': species.short_description,
    #         'disallowed_careers': species.disallowed_careers,
    #         'skills': species.skills,
    #         'talents': species.talents,
    #     }
    #     return initial_data


class SpeciesUpdateView(LoginRequiredMixin, UpdateView):
    model = Species
    form_class = SpeciesModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('species-list')


class SpeciesDeleteView(LoginRequiredMixin, DeleteView):
    model = Species
    template_name = 'form_confirm_delete.html'

    login_url = 'login'
    success_url = reverse_lazy('species-list')


class SpeciesDetailView(LoginRequiredMixin, DetailView):
    model = Species
    template_name = 'species-detail-view.html'
    context_object_name = 'species'

    login_url = 'login'


class ClassListView(LoginRequiredMixin, ListView):
    model = Class
    template_name = 'dashboard.html'
    paginate_by = 15

    success_url = reverse_lazy('class-list')

    def get_queryset(self):
        return Class.objects.filter(Q(author__isnull=True) | Q(author=self.request.user)).order_by('name')


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    form_class = ClassModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('class-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.success_url)

    def get_initial(self):
        class_ = get_object_or_404(Class, id=self.kwargs['pk'])
        initial_data = {
            'name': class_.name,
            'description': class_.description,
            'short_description': class_.short_description,
        }
        return initial_data


class ClassUpdateView(LoginRequiredMixin, UpdateView):
    model = Class
    form_class = ClassModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('class-list')


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Class
    template_name = 'form_confirm_delete.html'

    login_url = 'login'
    success_url = reverse_lazy('class-list')


class ClassDetailView(LoginRequiredMixin, DetailView):
    model = Class
    template_name = 'class-detail-view.html'
    context_object_name = 'class'

    login_url = 'login'


class CareerListView(LoginRequiredMixin, ListView):
    model = Career
    template_name = 'dashboard.html'
    paginate_by = 15

    login_url = 'login'

    def get_queryset(self):
        return Career.objects.filter(Q(author__isnull=True) | Q(author=self.request.user)).order_by('name')


class CareerCreateView(LoginRequiredMixin, CreateView):
    model = Career
    form_class = CareerModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('career-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.success_url)


class CareerUpdateView(LoginRequiredMixin, UpdateView):
    model = Career
    form_class = CareerModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('career-list')


class CareerDeleteView(LoginRequiredMixin, DeleteView):
    model = Career
    template_name = 'form_confirm_delete.html'

    login_url = 'login'
    success_url = reverse_lazy('career-list')


class CareerDetailView(LoginRequiredMixin, DetailView):
    model = Career
    template_name = 'career-detail-view.html'
    context_object_name = 'career'

    login_url = 'login'


class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'dashboard.html'
    paginate_by = 15

    def get_queryset(self):
        return Skill.objects.filter(Q(author__isnull=True) | Q(author=self.request.user)).order_by('name')


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('skill-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.success_url)

    def get_initial(self):
        skill = get_object_or_404(Skill, id=self.kwargs['pk'])
        initial_data = {
            'name': skill.name,
            'description': skill.description,
            'short_description': skill.short_description,
            'characteristic': skill.characteristic,
            'is_advanced': skill.is_advanced,
            'is_grouped': skill.is_grouped,
        }
        return initial_data


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('skill-list')


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    template_name = 'form_confirm_delete.html'

    login_url = 'login'
    success_url = reverse_lazy('skill-list')


class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    template_name = 'skill-detail-view.html'
    context_object_name = 'skill'

    login_url = 'login'


class TalentListView(LoginRequiredMixin, ListView):
    model = Talent
    template_name = 'dashboard.html'
    paginate_by = 15

    login_url = 'login'

    def get_queryset(self):
        return Talent.objects.filter(Q(author__isnull=True) | Q(author=self.request.user)).order_by('name')


class TalentCreateView(LoginRequiredMixin, CreateView):
    model = Talent
    form_class = TalentModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('talent-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.success_url)

    def get_initial(self):
        talent = get_object_or_404(Talent, id=self.kwargs['pk'])
        initial_data = {
            'name': talent.name,
            'description': talent.description,
            'short_description': talent.short_description,
            'tests': talent.tests,
            'bonus_when_maxed': talent.bonus_when_maxed,
            'level': talent.level,
        }
        return initial_data


class TalentUpdateView(LoginRequiredMixin, UpdateView):
    model = Talent
    form_class = TalentModelForm
    template_name = 'form.html'

    login_url = 'login'
    success_url = reverse_lazy('talent-list')


class TalentDeleteView(LoginRequiredMixin, DeleteView):
    model = Talent
    template_name = 'form_confirm_delete.html'

    login_url = 'login'
    success_url = reverse_lazy('talent-list')


class TalentDetailView(LoginRequiredMixin, DetailView):
    model = Talent
    template_name = 'talent-detail-view.html'
    context_object_name = 'talent'

    login_url = 'login'
