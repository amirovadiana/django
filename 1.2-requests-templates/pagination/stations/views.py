from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

list_stations = []


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_stations.append(row)
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list_stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': list_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
