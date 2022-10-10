from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.contrib.auth.views import LoginView


class RegisterUserView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'form.html'


class LoginUserView(LoginView):
    template_name = 'form.html'
