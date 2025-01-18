from django import forms
class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=30, label='Имя с тг')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')