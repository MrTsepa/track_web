from django.apps import apps
from django.shortcuts import get_object_or_404, resolve_url
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from .models import Task
from .forms import AceEditorForm

# Create your views here.


class TaskList(ListView):
    template_name = 'tasks/task_list.html'
    model = Task


class TaskDetailAndCreate(CreateView):
    model = apps.get_model('solutions.Solution')
    template_name = 'tasks/task_detail_and_create.html'
    fields = ('code', )

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.task = get_object_or_404(Task, id=pk)
        if self.request.user.is_authenticated:
            print self.request.user.is_authenticated
            self.task.user_solutions = self.task.solutions.filter(user=self.request.user)
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


class TaskDetailAceEditorView(FormView):
    form_class = AceEditorForm
    template_name = "tasks/task_detail_ace_editor.html"

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.task = get_object_or_404(Task, id=pk)
        if self.request.user.is_authenticated:
            self.task.user_solutions = self.task.solutions.filter(user=self.request.user)
        return super(TaskDetailAceEditorView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TaskDetailAceEditorView, self).get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_success_url(self):
        return resolve_url('tasks:task_detail_ace_editor', pk=self.task.id)

    def form_valid(self, form):
        solution = apps.get_model('solutions.Solution')()
        solution.user = self.request.user
        solution.task = self.task
        solution.code = form.cleaned_data['text']
        solution.save()
        return super(TaskDetailAceEditorView, self).form_valid(form)