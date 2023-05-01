from django import forms

from account.models import User


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()




class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',]
