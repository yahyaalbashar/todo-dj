from django.urls import path
from app.views import TaskList, TaskDetail, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/new/', TaskCreate.as_view(), name='task_new'),
    path('task/<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
]
