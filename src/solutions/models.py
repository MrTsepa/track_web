from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Solution(models.Model):
    task = models.ForeignKey('tasks.Task', related_name='solutions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    code = models.TextField()
    status = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "id: " + unicode(self.id) + ", " + \
               "Task: " + unicode(self.task)
