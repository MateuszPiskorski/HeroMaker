from django import forms
from django.forms import HiddenInput

from .models import Game


class GameModelForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
        widgets = {'author': HiddenInput()}
