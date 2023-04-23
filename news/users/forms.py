from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import logout

from .models import Profile


class CustomPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(
        label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")

    def clean(self):
        cleaned_data = super().clean()
        user = self.user
        new = cleaned_data.get('new_password1')
        logout()
        if user.check_password(new):
            raise ValidationError('New password matches the old one!')
        else:
            return cleaned_data


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']
