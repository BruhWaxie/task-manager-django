from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUSES = {
        'on_progress': 'On Progress',
        'completed': 'Completed',
        'not_started': 'Not started'
    }

    PRIORITIES = {
        'low': 'Low priority',
        'high': 'High priority',
        'medium': 'Medium priority'
    }

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=255, choices=STATUSES, default='not_started')
    priority = models.CharField(max_length=255, choices=PRIORITIES, default='low')

    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    image = models.ImageField()
    file = models.FileField(blank=True, null=True, upload_to='task_files/')

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    content = models.TextField()
    file = models.FileField(blank=True, null=True, upload_to='task_files/')
    
    def __str__(self):
        return f'Comment by {self.user} to {self.task}'