from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Solution(models.Model):
    task = models.ForeignKey('tasks.Task', related_name='solutions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    code = models.TextField()
    status = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)

    def run_tests(self):
        self.status = 'In progress'
        self.save()

        def handle_tests_results(solution):
            from src.buisness.executing import execute
            results = execute(solution.code, solution.task.tests.all())
            from src.buisness.testing import ResultType
            result = ResultType.OK
            for r in results:
                if r != ResultType.OK:
                    result = r
            self.status = result.name
            self.save()

        import threading
        thread = threading.Thread(target=handle_tests_results, args=[self])
        thread.start()

    def __unicode__(self):
        return "id: " + unicode(self.id) + ", " + \
               "Task: " + unicode(self.task)