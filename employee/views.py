from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee/list.html'
    context_object_name = 'employees'

class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/form.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'employee.add_employee'

class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/form.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'employee.change_employee'

class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Employee
    template_name = 'employee/confirm_delete.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'employee.delete_employee'
