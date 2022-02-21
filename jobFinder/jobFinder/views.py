from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import render
from account.models import *
from django.contrib.auth.models import User, auth

def home(request):
    if User.is_anonymous: 
        jobs = Vacancies.objects.all().order_by('-date')
        return render(request, 'home.html', {'jobs': jobs})
        
    else: 
        return render(request, 'dashboard.html')

def index(request):
    return render(request, 'index.html')