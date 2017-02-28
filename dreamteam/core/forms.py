from django import forms
from dreamteam.core.models import (UserMember, Team)
from django.contrib.auth.forms import UserChangeForm

class UserMemberForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta(UserChangeForm.Meta):
        model = UserMember
        fields = ('first_name', 'last_name', 'email', 'password', 'team')

    def __init__(self, *args, **kwargs):
        # self.entry = kwargs.pop('entry')   # the blog entry instance
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserMemberForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserMemberForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        # self.entry = kwargs.pop('entry')   # the blog entry instance
        super().__init__(*args, **kwargs)
