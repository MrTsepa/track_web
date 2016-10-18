from django.shortcuts import render
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
