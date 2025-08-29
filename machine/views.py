from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Machine, CalibrationEquipment
from .forms import MachineForm, MachineFilterForm, CalibrationDataForm, CalibrationEquipmentForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.conf import settings
from datetime import datetime
from calibrate.models import CalibrationForce, CalibrationPressure, CalibrationTorque

class MachineListView(LoginRequiredMixin, ListView):
    model = Machine
    template_name = 'machine/list.html'
    context_object_name = 'machines'
    
    def get_queryset(self):
        queryset = Machine.objects.filter(deleted=False)
        
        # รับพารามิเตอร์การกรอง
        organize_id = self.request.GET.get('organize_id')
        machine_type = self.request.GET.get('machine_type')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        serial_search = self.request.GET.get('serial_search')
        name_search = self.request.GET.get('name_search')
        
        # กรองตามหน่วยงาน
        if organize_id:
            queryset = queryset.filter(organize_id=organize_id)
        
        # กรองตามประเภทเครื่องมือ
        if machine_type:
            queryset = queryset.filter(machine_type_id=machine_type)
        
        # กรองตามวันที่
        if date_from:
            queryset = queryset.filter(update__gte=date_from)
        if date_to:
            queryset = queryset.filter(update__lte=date_to)
        
        # ค้นหา Serial Number
        if serial_search:
            queryset = queryset.filter(serial_number__icontains=serial_search)
        
        # ค้นหาชื่อเครื่องมือ
        if name_search:
            queryset = queryset.filter(name__icontains=name_search)
        

        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = MachineFilterForm(self.request.GET)
        
        # เพิ่มข้อมูลหน่วยงานสำหรับ dropdown
        from organize.models import Organize
        context['organizes'] = Organize.objects.all()
        context['selected_organize_id'] = self.request.GET.get('organize_id', '')
        
        return context

class MachineCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine/form.html'
    success_url = reverse_lazy('machine-list')
    permission_required = 'machine.add_machine'

class MachineUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine/form.html'
    success_url = reverse_lazy('machine-list')
    permission_required = 'machine.change_machine'

class MachineDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Machine
    template_name = 'machine/confirm_delete.html'
    success_url = reverse_lazy('machine-list')
    permission_required = 'machine.delete_machine'

@login_required
def send_machine_email(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == 'POST':
        from .forms import SendMachineEmailForm
        form = SendMachineEmailForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            subject = f"ข้อมูลเครื่องมือ: {machine.name}"
            body = f"ชื่อเครื่องมือ: {machine.name}\nรุ่น: {machine.model}\nหมายเลขเครื่อง: {machine.serial_number}\n" \
                   f"ประเภท: {machine.machine_type}\nหน่วยนับ: {machine.unit}\nผู้ผลิต: {machine.manufacture}\n" \
                   f"{message}"
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            return render(request, 'machine/send_email_done.html', {'machine': machine})
    else:
        from .forms import SendMachineEmailForm
        form = SendMachineEmailForm()
    return render(request, 'machine/send_email.html', {'form': form, 'machine': machine})

@login_required
def calibration_data(request, pk):
    """บันทึกการปรับเทียบ - redirect ไปยังระบบการปรับเทียบใหม่"""
    machine = get_object_or_404(Machine, pk=pk)
    return redirect('machine-calibration-list', machine_id=pk)

@login_required
def send_filtered_email(request):
    """ส่งอีเมลข้อมูลเครื่องมือที่กรองแล้ว"""
    if request.method == 'POST':
        # รับพารามิเตอร์การกรองจากฟอร์ม
        organize_id = request.POST.get('organize_id')
        machine_type = request.POST.get('machine_type')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        serial_search = request.POST.get('serial_search')
        name_search = request.POST.get('name_search')
        
        # สร้าง queryset ตามการกรอง
        queryset = Machine.objects.filter(deleted=False)
        
        if organize_id:
            queryset = queryset.filter(organize_id=organize_id)
        if machine_type:
            queryset = queryset.filter(machine_type_id=machine_type)
        if date_from:
            queryset = queryset.filter(update__gte=date_from)
        if date_to:
            queryset = queryset.filter(update__lte=date_to)
        if serial_search:
            queryset = queryset.filter(serial_number__icontains=serial_search)
        if name_search:
            queryset = queryset.filter(name__icontains=name_search)
        
        # สร้างเนื้อหาอีเมล
        subject = "รายงานเครื่องมือวัด"
        body = "รายการเครื่องมือวัดตามเงื่อนไขที่กรอง:\n\n"
        
        for machine in queryset:
            body += f"ID: {machine.id}\n"
            body += f"ชื่อเครื่องมือ: {machine.name}\n"
            body += f"รุ่น: {machine.model}\n"
            body += f"Serial Number: {machine.serial_number}\n"
            body += f"ประเภท: {machine.machine_type}\n"
            body += f"หน่วยนับ: {machine.unit}\n"
            body += f"ผู้ผลิต: {machine.manufacture}\n"
            body += f"วันที่อัปเดต: {machine.update}\n"
            body += "-" * 50 + "\n"
        
        # ส่งอีเมล
        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            messages.success(request, 'ส่งอีเมลรายงานสำเร็จ')
        except Exception as e:
            messages.error(request, f'เกิดข้อผิดพลาดในการส่งอีเมล: {str(e)}')
    
    return redirect('machine-list')

@login_required
def create_calibration_request(request, pk):
    """สร้างคำร้องขอบันทึกปรับเทียบสำหรับเครื่องมือ"""
    machine = get_object_or_404(Machine, id=pk)
    
    # รับ priority จาก URL parameter
    priority = request.GET.get('priority', 'normal')
    
    # ตรวจสอบประเภทเครื่องมือ
    machine_type_name = machine.machine_type.name.lower()
    
    try:
        # สร้างบันทึกการปรับเทียบตามประเภทเครื่องมือ
        if 'force' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = CalibrationForce.objects.filter(
                uuc_id=machine,
                status='pending'
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกปรับเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = CalibrationForce.objects.create(
                uuc_id=machine,
                status='pending',
                priority=priority
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกปรับเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        elif 'pressure' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = CalibrationPressure.objects.filter(
                uuc_id=machine,
                status='pending'
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกปรับเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = CalibrationPressure.objects.create(
                uuc_id=machine,
                status='pending',
                priority=priority
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกปรับเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        elif 'torque' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = CalibrationTorque.objects.filter(
                uuc_id=machine,
                status__in=['pending', 'not_set']
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกปรับเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = CalibrationTorque.objects.create(
                uuc_id=machine,
                status='not_set',
                priority=priority
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกปรับเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        else:
            messages.error(request, 'ไม่พบประเภทการปรับเทียบที่เหมาะสมสำหรับเครื่องมือนี้')
            return redirect('machine-list')
        
        return redirect('machine-list')
        
    except Exception as e:
        messages.error(request, f'เกิดข้อผิดพลาดในการส่งคำร้องขอ: {str(e)}')
        return redirect('machine-list')

# CalibrationEquipment Views
class CalibrationEquipmentListView(LoginRequiredMixin, ListView):
    model = CalibrationEquipment
    template_name = 'machine/calibration_equipment_list.html'
    context_object_name = 'calibration_equipment'
    
    def get_queryset(self):
        queryset = CalibrationEquipment.objects.all()
        
        # รับพารามิเตอร์การกรอง
        machine_type = self.request.GET.get('machine_type')
        name_search = self.request.GET.get('name_search')
        serial_search = self.request.GET.get('serial_search')
        
        # กรองตามประเภทเครื่องมือ
        if machine_type:
            queryset = queryset.filter(machine_type_id=machine_type)
        
        # ค้นหาชื่อเครื่องมือ
        if name_search:
            queryset = queryset.filter(name__icontains=name_search)
        
        # ค้นหา Serial Number
        if serial_search:
            queryset = queryset.filter(serial_number__icontains=serial_search)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import MachineType
        context['machine_types'] = MachineType.objects.all()
        return context

class CalibrationEquipmentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CalibrationEquipment
    form_class = CalibrationEquipmentForm
    template_name = 'machine/calibration_equipment_form.html'
    success_url = reverse_lazy('calibration-equipment-list')
    permission_required = 'machine.add_calibrationequipment'

class CalibrationEquipmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CalibrationEquipment
    form_class = CalibrationEquipmentForm
    template_name = 'machine/calibration_equipment_form.html'
    success_url = reverse_lazy('calibration-equipment-list')
    permission_required = 'machine.change_calibrationequipment'

class CalibrationEquipmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CalibrationEquipment
    template_name = 'machine/calibration_equipment_confirm_delete.html'
    success_url = reverse_lazy('calibration-equipment-list')
    permission_required = 'machine.delete_calibrationequipment'
