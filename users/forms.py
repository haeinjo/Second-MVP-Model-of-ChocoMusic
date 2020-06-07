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
        self.fields["avatar"].widget.attrs.update({"class": "fst-hidden"})
