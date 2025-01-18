from django import forms

class ReviewForm(forms.Form):
    user = forms.CharField(max_length=30, label='Имя с которого вы заходили на сайте:')
    content = forms.CharField(label='Текст отзыва:')