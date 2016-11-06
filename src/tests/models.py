from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Test(models.Model):
    input = models.TextField()
    output = models.TextField()
    task = models.ForeignKey('tasks.Task', related_name='tests')

    def __unicode__(self):
        return "id: " + unicode(self.id) + ", " + \
           "Task: " + unicode(self.task)
