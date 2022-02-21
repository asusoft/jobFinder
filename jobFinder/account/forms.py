from django import forms
from .models import *
from django.db import models


class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    current_job_sts = models.CharField(max_length=100)

#class JobForm(forms.ModelForm):
#    Title = forms.CharField()
#
#    class Meta:
#        model = Vacancies
#        fields = ('description',)