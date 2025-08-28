from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Comment

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
# Create your views here.
