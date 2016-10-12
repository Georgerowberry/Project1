from __future__ import unicode_literals
from time import time
from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    prefix = models.CharField(max_length=5)
    tel_number = models.CharField(max_length=11)
    position = models.CharField(max_length=35)
    email = models.CharField(max_length=35)
    picture = models.CharField(max_length=1000)

    def __str__ (self):
        return self.first_name + '  ' + self.last_name


