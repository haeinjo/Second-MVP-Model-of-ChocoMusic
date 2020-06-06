from django import forms
from . import models as user_models


class MusicianInfoForm(forms.ModelForm):
    class Meta:
        model = user_models.User
        fields = (
            "alias",
            "avatar",
            "borough",
        )

    def __init__(self, *args, **kwargs):
        super(MusicianInfoForm, self).__init__(*args, **kwargs)
        self.fields["alias"].widget.attrs.update({"class": "fst-input"})
        self.fields["alias"].widget.attrs["placeholder"] = "활동명을 입력해주세요."
        self.fields["avatar"].required = False
        self.fields["borough"].required = False
        self.fields["borough"].widget = forms.CheckboxSelectMultiple
        self.fields["borough"].choices = None
        self.fields["avatar"].widget.attrs.update({"id": "fst-hidden-input"})

        # def clean(self):
        #     alias = self.cleaned_data.get("alias")
        #     genre = self.cleaned_data.get("genre")
        #     position = self.cleaned_data.get("position")

        #     return self.cleaned_data
