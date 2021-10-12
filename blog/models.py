from django.db import models
from django.conf import settings
from django.shortcuts import reverse

class Blog(models.Model):
    title = models.CharField(max_length=200)
    upload_date = models.DateField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    description = models.TextField()


