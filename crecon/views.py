# -*- coding: utf-8 -*-
import os
import csv
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Salestring
from .graphics import Graph, Metods
from .forms import SettingsForm


def home(request):
    return render(request, 'home.html', {})

def select(request):
    sell_object = Salestring.objects.order_by().values_list('title').distinct()
    selltable = []
    for index in range(len(sell_object)):
        selltable.append(sell_object[index][0])

    return render(request, 'select.html', {'table' : selltable})

def saleslist(request):
    g = Graph()
    try:
        shop = request.GET['shop']
        table_sales = Salestring.objects.filter(title=shop)
        context = g.get_context_data(table_sales)
        return render(request, 'data.html', {'table_sales': table_sales, 'graph': context})
    except:
        raise Http404("No shop matches the given query.")

def prognoz(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            for key, val in form.cleaned_data.items():
                setattr(Metods, key, val)

            try:
                shop = form.data['mag']
            except:
                raise Http404("No shop matches the given query.")

            g = Graph()
            table_sales = Salestring.objects.filter(title=shop)
            context = g.universal_prognoz(table_sales, Metods)

            return render(request, 'prognoz.html', {'table_sales': table_sales, 'graph': context})
        else:
            raise Http404("no valide form")
    else:
        raise Http404("fucking wrong.")

def select_prognoz(request):
    form = SettingsForm()

    sell_object = Salestring.objects.order_by().values_list('title').distinct()
    selltable = []
    for index in range(len(sell_object)):
        selltable.append(sell_object[index][0])

    return render(request, 'select_prognoz.html', {'table': selltable, 'settingsform': form})

def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        parsing_file(request.FILES['file'], str(request.FILES['file']))

        return HttpResponse("Successful")

    return HttpResponse("Failed")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def parsing_file(file, filename):
    with open('upload/' +filename) as f:
        reader = csv.reader(f,dialect='excel', delimiter=';')
        for row in reader:
            _, created = Salestring.objects.get_or_create(
                title=row[0],
                sale_date=row[1],
                day_code=row[2],
                sumsale=row[3],
            )