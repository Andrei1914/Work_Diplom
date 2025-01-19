#все библиотки
from .models import *
from .Forms import *
from django.shortcuts import render, redirect
from django.core.paginator import Paginator



#отображение главной старницы
def main_page(request):
    return render(request, 'main_page.html')


#отображение страницы с вопросами
def help_page(request):
    if request.method == 'POST': #условие на проверку метода запроса
        form = HelpForm(request.POST) #запись формы в саму перемнную для дальнешей работы с ней
        if form.is_valid(): #проверка на валидность формы
            username=form.cleaned_data['user'] #получение данных с поля user из формы HelpForm
            user = Users.objects.get(name=username) #провоерка на наличие пользователя в базе
            if user.is_verified: #проверка на верефицированность пользователя
                user_id = user.user_id  #получение user_id для записи юзера в бд
                Help.objects.create( #создание вопроса от пользователя
                    user_id=user_id,
                    message=form.cleaned_data['message'],
                    answer_message = ''
                )
                return redirect('help_page') #отображение страницы по имени юрл для избежания дабл форм
            else:
                # Если пользователь не верифицирован, возвращаем информацию
                return render(request, 'help.html', {
                    'info': 'Для того, чтобы задать вопрос, пожалуйста, войдите в аккаунт!',
                    'form': form,
                    'helps': get_paginated_helps(request)
                })
        else:
            # Если форма не валидна, возвращаем ошибки
            return render(request, 'help.html', {
                'form': form,
                'helps': get_paginated_helps(request),
                'info': 'Пожалуйста, исправьте ошибки в форме.'
            })
    else:
        #если запрос типа get, возвращаем страницу
        form = HelpForm()
        return render(request, 'help.html', {
            'form': form,
            'helps': get_paginated_helps(request)
        })
    
def get_paginated_helps(request): #функция для геи запросов с вопросами
    help = Help.objects.all().order_by('-date_publish')
    paginator = Paginator(help, 3)
    page_obj = paginator.get_page(request.GET.get('page'))
    return page_obj


def example_work_page(request): #функция для примеров работ
    categories = Category.objects.all() #запсиваем все категории в переменную
    selected_category = request.GET.get('category') #гет запрос с категорией


    if selected_category: #проверка на отображение по категориям или нет
        examples = WorkExample.objects.filter(category_id=selected_category)
    else:
        examples = WorkExample.objects.all()


    ex = Paginator(examples, 3) #пагинация, максимальное число отображаемых данныз - 3 запси
    page_obj = ex.get_page(request.GET.get('page'))
    context = { #добавление всех данных в переменную для дальнейшего редактирования в шаблоне
        'examples': examples,
        'categories': categories,
        'selected_category': selected_category,
        'reviews': page_obj,
    }

    return render(request, 'example_work_page.html', context) #отображение страницы с примерами работ

def service_manicure_page(request):
    return render(request, 'service_manicure.html')

def service_eyelash_page(request):
    return render(request, 'service_eyelash.html')

def service_cleaning_page(request):
    return render(request, 'service_cleaning.html')

def service_makeup_page(request):
    return render(request, 'service_makeup.html')

def login_user_page(request): # функция для врефикации пользователя
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = Users.objects.get(name=username, password=password)
            if user:
                user.is_verified = True
                user.save()
                return render(request, 'main_page.html', {'info': 'Вы вошли в свой аккаунт, теперь можете оставлять отзывы и задавать вопросы.'})
            else:
                return render(request, 'login.html', {'info': 'Неверный пароль! Или же пользователя нет в системе!'})

    form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def add_review_page(request): #аналогичная функция с help_page но тут я разделил уже на гет и пост запрос
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['user']
            user = Users.objects.get(name=username)
                
            if user.is_verified:
                Review.objects.create(
                    user=username,
                    content=form.cleaned_data['content']
                )
                return render(request, 'main_page.html', {'info':'Ваш отзыв успешно добавлен!'})
    else:
        form = ReviewForm()
        return render(request, 'add_review_page.html', {'form': form})

def review_page(request):  #аналогичная функция с help_page гет запрос
    reviews = Review.objects.all().order_by('date_publish')
    rv = Paginator(reviews, 3)
    page_obj = rv.get_page(request.GET.get('page'))

    return render(request, 'review_page.html', {'reviews': page_obj}) 