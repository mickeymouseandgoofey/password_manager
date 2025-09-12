from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Credential

# Form for adding credentials with plaintext password input
class CredentialForm(forms.ModelForm):
    password_plain = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="Enter the password you want to store."
    )

    class Meta:
        model = Credential
        fields = ['site_name', 'site_url', 'username', 'notes']

# Custom user registration form with no password length restriction
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="Enter any password—no length restrictions."
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        pw1 = self.cleaned_data.get("password1")
        pw2 = self.cleaned_data.get("password2")
        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("Passwords do not match.")
        return pw2
