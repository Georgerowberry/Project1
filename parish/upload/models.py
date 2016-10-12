from __future__ import unicode_literals
from time import time
from django.db import models


class File(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/%Y/%m/%d')


class Minuets(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='minuets/%Y/%m/%d')
    date = models.DateField()
