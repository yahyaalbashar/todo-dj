from django.views.generic.list import ListView

from app.models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
