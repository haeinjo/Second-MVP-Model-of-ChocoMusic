from django import forms
from . import models as user_models
from core import models as core_models

# from core import models as core_models


class UserLoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "이메일"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "패스워드"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = user_models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 틀립니다."))
        except user_models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("유저가 존재하지 않습니다."))


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = user_models.User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "이름"}),
            "last_name": forms.TextInput(attrs={"placeholder": "성"}),
            "email": forms.EmailInput(attrs={"placeholder": "이메일"}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 확인"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            user_models.User.objects.get(email=email)
            raise forms.ValidationError("이미 가입된 이메일 입니다", code="existing_user")
        except user_models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password == password1:
            return password
        else:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")

    def save(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = super().save(commit=False)
        user.username = email
        user.set_password(password)
        user.save()


class MusicianAliasForm(forms.Form):

    alias = forms.CharField(max_length=64, label="별명")
    avatar = forms.FileField()

    class Meta:
        def __init__(self, *args, **kwargs):
            self.fields["alias"].widget.attrs.update({"class": "form__input"})


class MusicianActiveRegionForm(forms.Form):

    boroughs = forms.ModelMultipleChoiceField(
        queryset=core_models.Borough.objects.all()
    )


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
        self.fields["alias"].widget.attrs.update({"class": "form__input"})
        self.fields["alias"].widget.attrs["placeholder"] = "활동명을 입력해주세요."
        # self.fields["avatar"].required = False
        self.fields["avatar"].widget.attrs.update({"class": "form--hidden"})
        self.fields["borough"].required = False
        self.fields["positions"].required = False
        self.fields["genres"].required = False
        self.fields["is_first"].initial = True
        # self.fields["borough"].queryset = core_models.Borough.objects.all()

    def clean_is_first(self):
        print(self.cleaned_data["genres"])
        if self.cleaned_data["genres"] is not None:
            self.is_first = False
        return self.is_first
