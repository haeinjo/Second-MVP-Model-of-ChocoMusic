from django import forms
from . import models as content_models


# from core import models as core_models


class ContentForm(forms.ModelForm):
    class Meta:
        model = content_models.Content
        fields = (
            "content_type",
            "content_file",
            "content_photo",
            "content_title",
            "genre",
            "description",
            "project",
            "exposure_level",
        )

    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)

        self.fields["content_photo"].required = False
        self.fields["content_title"].widget.attrs.update(
            {"class": "content-info-select"}
        )
        self.fields["genre"].widget.attrs.update({"class": "content-info-select"})
        self.fields["description"].required = False
        self.fields["description"].widget.attrs.update({"class": "content-info-select"})
        self.fields["project"].widget.attrs.update({"class": "content-info-select"})
        self.fields["exposure_level"].widget = forms.RadioSelect(
            choices=content_models.EXPOSURE_CHOICES
        )

    #     self.fields["alias"].widget.attrs.update({"class": "fst-input"})
    #     self.fields["alias"].widget.attrs["placeholder"] = "활동명을 입력해주세요."
    #     self.fields["avatar"].required = False
    #     self.fields["avatar"].widget.attrs.update({"class": "fst-hidden"})
    #     self.fields["borough"].required = False
    #     self.fields["positions"].required = False
    #     self.fields["genres"].required = False
    #     self.fields["is_first"].initial = True
    #     # self.fields["borough"].queryset = core_models.Borough.objects.all()

    # def clean_is_first(self):
    #     if self.cleaned_data["genres"] is not None:
    #         self.is_first = False
    #     return self.is_first
