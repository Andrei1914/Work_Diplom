
from .models import *
from .LoginForm import *
from .ReviewForm import *
from .HelpForms import *
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

def main_page(request):
    return render(request, 'main_page.html')



def help_page(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['user']
            user = Users.objects.get(name=username)
            if user.is_verified:
                user_id = user.user_id
                Help.objects.create(
                    user_id=user_id,
                    message=form.cleaned_data['message'],
                    answer_message = ''
                )
                return redirect('help_page')
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
        form = HelpForm()
        return render(request, 'help.html', {
            'form': form,
            'helps': get_paginated_helps(request)
        })
    
def get_paginated_helps(request):
    help = Help.objects.all().order_by('-date_publish')
    paginator = Paginator(help, 3)
    page_obj = paginator.get_page(request.GET.get('page'))
    return page_obj


def example_work_page(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')


    if selected_category:
        examples = WorkExample.objects.filter(category_id=selected_category)
    else:
        examples = WorkExample.objects.all()

    ex = Paginator(examples, 3)
    page_obj = ex.get_page(request.GET.get('page'))
    context = {
        'examples': examples,
        'categories': categories,
        'selected_category': selected_category,
        'reviews': page_obj,
    }

    return render(request, 'example_work_page.html', context) 

def service_manicure_page(request):
    return render(request, 'service_manicure.html')

def service_eyelash_page(request):
    return render(request, 'service_eyelash.html')

def service_cleaning_page(request):
    return render(request, 'service_cleaning.html')

def service_makeup_page(request):
    return render(request, 'service_makeup.html')

def login_user_page(request):
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

def add_review_page(request):
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

def review_page(request):
    reviews = Review.objects.all().order_by('date_publish')
    rv = Paginator(reviews, 3)
    page_obj = rv.get_page(request.GET.get('page'))

    return render(request, 'review_page.html', {'reviews': page_obj}) 