from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Standard
from .forms import StandardForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class StandardListView(LoginRequiredMixin, ListView):
    model = Standard
    template_name = 'std/list.html'
    context_object_name = 'standards'

class StandardCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Standard
    form_class = StandardForm
    template_name = 'std/form.html'
    success_url = reverse_lazy('std-list')
    permission_required = 'std.add_standard'

class StandardUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Standard
    form_class = StandardForm
    template_name = 'std/form.html'
    success_url = reverse_lazy('std-list')
    permission_required = 'std.change_standard'

class StandardDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Standard
    template_name = 'std/confirm_delete.html'
    success_url = reverse_lazy('std-list')
    permission_required = 'std.delete_standard' 