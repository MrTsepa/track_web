from django.apps import apps
from django.shortcuts import get_object_or_404, resolve_url, get_list_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Task


class TaskList(ListView):
    template_name = 'tasks/task_list.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        return context


class TaskDetailView(TemplateView):
    template_name = "tasks/task_detail.html"

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.task = get_object_or_404(Task, id=pk)
        self.tasks = get_list_or_404(Task)
        if self.request.user.is_authenticated:
            self.task.user_solutions = self.task.solutions.filter(user=self.request.user)
        return super(TaskDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['task'] = self.task
        context['tasks'] = self.tasks
        return context

    def get_success_url(self):
        return resolve_url('tasks:task_detail', pk=self.task.id)

    # def form_valid(self, form):
    #     solution = apps.get_model('solutions.Solution')()
    #     solution.user = self.request.user
    #     solution.task = self.task
    #     solution.code = form.cleaned_data['text']
    #     solution.save()
    #     solution.run_tests()
    #     return super(TaskDetailView, self).form_valid(form)