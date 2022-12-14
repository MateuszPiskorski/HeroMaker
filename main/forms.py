from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'description',
            'short_description',
            InlineCheckboxes('disallowed_careers'),
            InlineCheckboxes('skills'),
            InlineCheckboxes('talents'),
        )
        self.helper.add_input(Submit('submit', 'Submit'))


class ClassModelForm(forms.ModelForm):
    class Meta:
        model = Class
        exclude = ["author"]


class CareerModelForm(forms.ModelForm):
    class Meta:
        model = Career
        exclude = ["author"]
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
            'talents': forms.CheckboxSelectMultiple,
        }
        labels = {
            'class_for_career': 'Class',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'description',
            'short_description',
            'first_level_name',
            'class_for_career',
            InlineCheckboxes('skills'),
            InlineCheckboxes('talents'),
        )
        self.helper.add_input(Submit('submit', 'Submit'))


class SkillModelForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ["author"]


class TalentModelForm(forms.ModelForm):
    class Meta:
        model = Talent
        exclude = ["author"]
