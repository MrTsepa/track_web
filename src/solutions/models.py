from __future__ import unicode_literals

from django.db import models


class Solution(models.Model):
    task = models.ForeignKey('tasks.Task', related_name='solutions')
    user = models.ForeignKey('core.User')
    code = models.TextField()
    status = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)

    def run_tests(self):
        self.status = 'In progress'
        self.save()
        
        import threading

        def prepare_and_test(solution):
            from src.buisness.models import Code, Test
            from src.buisness.executing import execute
            code_path = 'data/solutions/' + str(solution.id) + '/code.py'
            with open(code_path, 'w+') as fout:
                fout.write(solution.code)
            code = Code(code_path)
            tests = []
            for test in solution.task.tests:
                tests.append(Test(str(test.input_path), str(test.output_path)))
            execute(code, tests)

        thread = threading.Thread(target=prepare_and_test, args=[self])
        # thread.start()

    def __unicode__(self):
        return "id: " + unicode(self.id) + ", " + \
               "Task: " + unicode(self.task)
