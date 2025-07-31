from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Organize
from .forms import OrganizeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class OrganizeListView(LoginRequiredMixin, ListView):
    model = Organize
    template_name = 'organize/list.html'
    context_object_name = 'organizes'

class OrganizeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Organize
    form_class = OrganizeForm
    template_name = 'organize/form.html'
    success_url = reverse_lazy('organize-list')
    permission_required = 'organize.add_organize'

class OrganizeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Organize
    form_class = OrganizeForm
    template_name = 'organize/form.html'
    success_url = reverse_lazy('organize-list')
    permission_required = 'organize.change_organize'

class OrganizeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Organize
    template_name = 'organize/confirm_delete.html'
    success_url = reverse_lazy('organize-list')
    permission_required = 'organize.delete_organize'
