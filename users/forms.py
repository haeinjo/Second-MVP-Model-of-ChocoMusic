from django import forms
from . import models as user_models


class MusicianInfoForm(forms.ModelForm):
    class Meta:
        model = user_models.User
        fields = ("alias", "genres", "positions")

        # def clean(self):
        #     alias = self.cleaned_data.get("alias")
        #     genre = self.cleaned_data.get("genre")
        #     position = self.cleaned_data.get("position")

        #     return self.cleaned_data
