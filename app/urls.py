"""
 Copyright (C) 2022 Hemant Sachdeva <hemant.evolver@gmail.com>

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
 """

from django.urls import path
from app.views import CustomLoginView, PasswordChangeSuccessView, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete
from app.forms import RegisterForm, PasswordChangeForm

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterForm.as_view(), name='register'),
    path('password_change/', PasswordChangeForm.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeSuccessView.as_view(), name='password_change_success'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/new/', TaskCreate.as_view(), name='task_new'),
    path('task/<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
]
