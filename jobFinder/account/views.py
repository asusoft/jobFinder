from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from .forms import *
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        company_id = request.POST['company_id']
        password = request.POST['password']

        user = auth.authenticate(username=company_id, password=password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('./dashboard')
           
        else:
            messages.info(request, 'Incorrect credentials')
            return redirect('./login')
    
    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        company_name = request.POST['company_name']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password == password1:
            if User.objects.filter(username=company_name).exists():
                messages.info(request, 'A user with the same company name exists')
                return redirect('./register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request, 'Email already in use')
                 return redirect('./register')
            else:
                user = User.objects.create_user( username = company_name,password = password,email = email)
                user.save()
                messages.info(request, 'Account successfully created')
                return redirect('./dashboard')
                
                
        
        else:
            messages.info(request, 'Password does not match')
            return redirect('./register')

       

    else:
        return render(request, 'signup.html')
   

def job(request, pk):
    job = Vacancies.objects.get(pk=pk)
    return render(request, 'job.html', {'job': job})

@login_required(login_url='/account/login')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/account/login')
def dashboard(request):
    jobs = Vacancies.objects.all().order_by('-date')
    return render(request, 'dashboard.html', {'jobs': jobs})

@login_required(login_url='/account/login')
def post(request):
    
    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']
        city = request.POST['city']
        country = request.POST['country']
        user = request.user

        Vacancies.objects.create(user = user, title =title, description = description, city = city, country = country)
        return redirect('./dashboard')
        #return redirect('/')

    return render(request, 'post.html')

    
def apply(request, pk):
    job = Vacancies.objects.get(pk=pk)
    return render(request, 'apply.html', {'job': job})