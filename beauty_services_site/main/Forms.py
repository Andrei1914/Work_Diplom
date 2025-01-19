from django import forms 


#Форма для составления вопросов от пользователя с полями user - Имя пользавтеля с основной бд и message - текст вопроса
class HelpForm(forms.Form):
    user = forms.CharField(max_length=30, label='Имя с которого вы заходили на сайте:')
    message = forms.CharField(label='Вопрос:')



#Форма для входа в аккаунт с полями name - Имя пользавтеля с основной бд и password - паролль пользователя
class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=30, label='Имя с тг')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')



#Форма для составления отзыва от пользователя с полями user - Имя пользавтеля и content - текст отзыва
class ReviewForm(forms.Form):
    user = forms.CharField(max_length=30, label='Имя с которого вы заходили на сайте:')
    content = forms.CharField(label='Текст отзыва:')