# crud_app/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'user', 'description']  # Add any additional fields as needed

    # Add custom validation or styling here if necessary
