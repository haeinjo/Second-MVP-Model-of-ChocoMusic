from django import forms
from . import models as user_models

# from core import models as core_models


class MusicianInfoForm(forms.ModelForm):
    class Meta:
        model = user_models.User
        fields = (
            "alias",
            "avatar",
            "borough",
            "positions",
            "genres",
            "is_first",
        )

    def __init__(self, *args, **kwargs):
        super(MusicianInfoForm, self).__init__(*args, **kwargs)
        self.fields["alias"].widget.attrs.update({"class": "fst-input"})
        self.fields["alias"].widget.attrs["placeholder"] = "활동명을 입력해주세요."
        self.fields["avatar"].required = False
        self.fields["avatar"].widget.attrs.update({"class": "fst-hidden"})
        self.fields["borough"].required = False
        self.fields["positions"].required = False
        self.fields["genres"].required = False
        self.fields["is_first"].initial = True
        # self.fields["borough"].queryset = core_models.Borough.objects.all()

    def clean_is_first(self):
        if self.cleaned_data["genres"] is not None:
            self.is_first = False
        return self.is_first
