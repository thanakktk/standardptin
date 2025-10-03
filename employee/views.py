from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from accounts.permissions import PermissionRequiredMixin as CustomPermissionRequiredMixin

User = get_user_model()

class EmployeeListView(LoginRequiredMixin, CustomPermissionRequiredMixin, ListView):
    model = User
    template_name = 'employee/list.html'
    context_object_name = 'employees'
    permission_required = 'view_users'
    
    def get_queryset(self):
        return User.objects.filter(is_active=True).order_by('username')

class EmployeeCreateView(LoginRequiredMixin, CustomPermissionRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'employee/form.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'manage_users'

class EmployeeUpdateView(LoginRequiredMixin, CustomPermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'employee/form.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'manage_users'

class EmployeeDeleteView(LoginRequiredMixin, CustomPermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'employee/confirm_delete.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'manage_users'
