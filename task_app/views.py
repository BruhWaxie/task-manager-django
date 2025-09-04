from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Task, Comment
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
# Create your views here.

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_created.html'
    fields = ('title', 'description', 'status', 'priority', 'deadline', 'image', 'file')

    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    fields = ('title', 'description', 'status', 'priority', 'deadline', 'image', 'file')

    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)