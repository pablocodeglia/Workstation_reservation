from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


"""
Custom UserCreationForm to check submitted email against the one in 
the employees record (corporate email)
"""
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'email', 'password1', 'password2' ]


    def clean_email(self):

        email = self.cleaned_data.get("email").strip().lower()

        if not email.endswith("@corporation.com"):
            raise forms.ValidationError('Must use your corporate email (employee@corporation.com)')
        return email
