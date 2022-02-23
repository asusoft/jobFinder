from django.db import models
from django.contrib.auth.models import User
from .forms import Applicant

# Create your models here.
    
class Vacancies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    applicants = models.ManyToManyField(Applicant,  related_name='job_post')
