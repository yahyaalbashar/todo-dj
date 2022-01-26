from django.urls import path
from app.views import CustomLoginView, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/new/', TaskCreate.as_view(), name='task_new'),
    path('task/<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
]
