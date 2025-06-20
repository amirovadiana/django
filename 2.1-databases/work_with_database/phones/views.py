from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    products_all = Phone.objects.all()
    sort_by = request.GET.get('sort')
    template = 'catalog.html'

    if sort_by == 'name':
        phones = products_all.order_by('name')
    elif sort_by == 'min_price':
        phones = products_all.order_by('price')
    elif sort_by == 'max_price':
        phones = products_all.order_by('-price')

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug__contains=slug).first()
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
