from django.db import models

# Create your models here.

class Opening(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    
    