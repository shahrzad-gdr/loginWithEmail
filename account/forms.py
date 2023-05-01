from django.forms import forms
from account.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password',]


