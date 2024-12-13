# crud_app/admin.py
from django.contrib import admin
from .models import Task
from .forms import TaskForm

class TaskAdmin(admin.ModelAdmin):
    form = TaskForm  # Use the custom form for task creation and editing
    list_display = ('title', 'status', 'user')
    list_filter = ('status', 'user')
    search_fields = ('title', 'status')


admin.site.register(Task, TaskAdmin)
