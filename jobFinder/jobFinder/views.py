from django.http import HttpResponse
from django.shortcuts import render
from account.models import Opening

def home(request):

    jobs = Opening.objects.all()
    return render(request, 'home.html', {'jobs': jobs})

def index(request):
    return render(request, 'index.html')