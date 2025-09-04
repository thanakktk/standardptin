from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

User = get_user_model()

class EmployeeListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'employee/list.html'
    context_object_name = 'employees'
    
    def get_queryset(self):
        return User.objects.filter(is_active=True).order_by('username')

class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'employee/form.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'accounts.add_user'

class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'employee/form.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'accounts.change_user'

class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'employee/confirm_delete.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'accounts.delete_user'
