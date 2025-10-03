from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Organize
from .forms import OrganizeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from accounts.permissions import PermissionRequiredMixin as CustomPermissionRequiredMixin

class OrganizeListView(LoginRequiredMixin, CustomPermissionRequiredMixin, ListView):
    model = Organize
    template_name = 'organize/list.html'
    context_object_name = 'organizes'
    permission_required = 'view_organization'

class OrganizeCreateView(LoginRequiredMixin, CustomPermissionRequiredMixin, CreateView):
    model = Organize
    form_class = OrganizeForm
    template_name = 'organize/form.html'
    success_url = reverse_lazy('organize-list')
    permission_required = 'manage_organization'

class OrganizeUpdateView(LoginRequiredMixin, CustomPermissionRequiredMixin, UpdateView):
    model = Organize
    form_class = OrganizeForm
    template_name = 'organize/form.html'
    success_url = reverse_lazy('organize-list')
    permission_required = 'manage_organization'

class OrganizeDeleteView(LoginRequiredMixin, CustomPermissionRequiredMixin, DeleteView):
    model = Organize
    template_name = 'organize/confirm_delete.html'
    success_url = reverse_lazy('organize-list')
    permission_required = 'manage_organization'
