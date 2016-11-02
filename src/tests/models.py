from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Test(models.Model):
    input_path = models.CharField(max_length=256)
    output_path = models.CharField(max_length=256)
    task = models.ForeignKey('tasks.Task', related_name='tests')

    def __unicode__(self):
        return "id: " + unicode(self.id) + ", " + \
           "Task: " + unicode(self.task)
