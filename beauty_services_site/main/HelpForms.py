from django import forms 

class HelpForm(forms.Form):
    user = forms.CharField(max_length=30, label='Имя с которого вы заходили на сайте:')
    message = forms.CharField(label='Вопрос:')