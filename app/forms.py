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

from django.shortcuts import redirect
from django.contrib.auth import login, update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterForm(FormView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterForm, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterForm, self).get(*args, **kwargs)


class PasswordChangeForm(LoginRequiredMixin, FormView):
    template_name = 'app/password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_success')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            update_session_auth_hash(self.request, user)
        return super(PasswordChangeForm, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeForm, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
