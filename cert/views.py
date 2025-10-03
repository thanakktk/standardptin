from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Certificate
from .forms import CertificateForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class CertificateListView(LoginRequiredMixin, ListView):
    model = Certificate
    template_name = 'cert/list.html'
    context_object_name = 'certificates'
    
    def get_queryset(self):
        queryset = Certificate.objects.all()
        
        # กรองตามหน่วยงานของผู้ใช้ (สำหรับหน่วยผู้ใช้)
        user = self.request.user
        if user.is_unit_user() and not user.is_superuser:
            # หน่วยผู้ใช้เห็นเฉพาะใบรับรองของเครื่องมือในหน่วยตัวเอง
            if user.organize:
                queryset = queryset.filter(machine__organize=user.organize)
            else:
                # ถ้าไม่มีหน่วยงาน ให้แสดงข้อมูลว่าง
                queryset = queryset.none()
        
        return queryset

class CertificateCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Certificate
    form_class = CertificateForm
    template_name = 'cert/form.html'
    success_url = reverse_lazy('cert-list')
    permission_required = 'cert.add_certificate'

class CertificateUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Certificate
    form_class = CertificateForm
    template_name = 'cert/form.html'
    success_url = reverse_lazy('cert-list')
    permission_required = 'cert.change_certificate'

class CertificateDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Certificate
    template_name = 'cert/confirm_delete.html'
    success_url = reverse_lazy('cert-list')
    permission_required = 'cert.delete_certificate'
