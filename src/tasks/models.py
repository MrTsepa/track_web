from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    difficulty = models.IntegerField()
