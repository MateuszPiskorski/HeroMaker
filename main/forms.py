from django import forms
from .models import Game, Species, Class, Skill, Talent, Career


class GameModelForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ["author"]


class SpeciesModelForm(forms.ModelForm):
    class Meta:
        model = Species
        exclude = ["author"]
        widgets = {
            'disallowed_careers': forms.CheckboxSelectMultiple,
            'skills': forms.CheckboxSelectMultiple,
            'talents': forms.CheckboxSelectMultiple,
        }


class ClassModelForm(forms.ModelForm):
    class Meta:
        model = Class
        exclude = ["author"]


class CareerModelForm(forms.ModelForm):
    class Meta:
        model = Career
        exclude = ["author"]


class SkillModelForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ["author"]


class TalentModelForm(forms.ModelForm):
    class Meta:
        model = Talent
        exclude = ["author"]
