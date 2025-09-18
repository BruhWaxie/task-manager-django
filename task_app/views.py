from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, Comment
from .forms import TaskForm, FilterForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        
        tasks =  Task.objects.filter(user=self.request.user).all()
        status = self.request.GET.get('status', '')
        priority = self.request.GET.get('priority', '')

        if status:
            tasks = tasks.filter(status=status)

        if priority:
            tasks = tasks.filter(priority=priority)

        return tasks
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterForm'] = FilterForm(self.request.GET)
        return context
# Create your views here.

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_created.html'
    success_url = reverse_lazy('Home')

    ordering = ['-created-at']


    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    success_url = reverse_lazy('Home')  

    form_class = TaskForm

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('Home')

    