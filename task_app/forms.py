from django import forms
from .models import Task # Припустимо, у вас є модель Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', 'status', 'file', 'image'] # Поля для форми


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2', })

        self.fields['deadline'].widget = forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control mb-2'})