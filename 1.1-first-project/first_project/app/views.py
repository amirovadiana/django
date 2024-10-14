from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_date = datetime.datetime.now()
    current_time = current_date.time().strftime('%H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    template_name = 'app/workdir.html'
    directory = r'C:\Users\Diana\Desktop\Home_Works\gjango\1.1-first-project\first_project'
    pages = {}
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            pages[filename] = ''
        else:
            val = []
            val += os.listdir(filename)
            pages[filename] = val

    del pages['.idea']
    del pages['.venv']

    context = {
        'pages': pages
    }
    return render(request, template_name, context)
