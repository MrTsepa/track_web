from django.apps import apps
from django.shortcuts import get_object_or_404, resolve_url
from django.views.generic.edit import CreateView

from .models import Task
from django.views.generic.list import ListView
from django.views.generic import DetailView

# Create your views here.


class TaskList(ListView):
    template_name = 'tasks/task_list.html'
    model = Task


class TaskDetail(DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task


class TaskDetailAndCreate(CreateView):
    model = apps.get_model('solutions.Solution')
    template_name = 'tasks/task_detail_and_create.html'
    fields = ('code', )

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.task = get_object_or_404(Task, id=pk)
        return super(TaskDetailAndCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TaskDetailAndCreate, self).get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_success_url(self):
        return resolve_url('tasks:task_detail_and_create', pk=self.object.task.id)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.task = self.task
        return super(TaskDetailAndCreate, self).form_valid(form)
