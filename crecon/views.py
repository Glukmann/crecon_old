# -*- coding: utf-8 -*-
import os
import csv
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def base(request):
    return render(request, 'base.html', {})
