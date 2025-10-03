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
from calibrate.models import CalibrationPressure, CalibrationTorque, BalanceCalibration, MicrowaveCalibration, HighFrequencyCalibration, LowFrequencyCalibration, DialGaugeCalibration
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from accounts.permissions import PermissionRequiredMixin, permission_required
import json

class MachineListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Machine
    template_name = 'machine/list.html'
    context_object_name = 'machines'
    permission_required = 'view_machine'
    
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
    permission_required = 'add_machine'

class MachineUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine/form.html'
    success_url = reverse_lazy('machine-list')
    permission_required = 'edit_machine'

class MachineDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Machine
    template_name = 'machine/confirm_delete.html'
    success_url = reverse_lazy('machine-list')
    permission_required = 'delete_machine'

@login_required
@permission_required('send_notification')
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
            
            # ส่งอีเมลไปที่หน่วยงานของเครื่องมือเท่านั้น
            recipient_emails = []
            if machine.organize and machine.organize.email:
                recipient_emails.append(machine.organize.email)
            else:
                # ถ้าไม่มีอีเมลหน่วยงาน ให้แสดงข้อความแจ้งเตือน
                messages.warning(request, 'ไม่พบอีเมลของหน่วยงาน กรุณาเพิ่มอีเมลหน่วยงานก่อน')
                return render(request, 'machine/send_email.html', {'form': form, 'machine': machine})
            
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    recipient_emails,
                    fail_silently=False,
                )
                messages.success(request, f'ส่งอีเมลสำเร็จไปยัง {", ".join(recipient_emails)}')
            except Exception as e:
                messages.warning(request, f'ไม่สามารถส่งอีเมลผ่าน SMTP ได้: {str(e)}')
                # เก็บอีเมลเป็นไฟล์แทน
                try:
                    import datetime
                    
                    # สร้างโฟลเดอร์ sent_emails ถ้าไม่มี
                    email_dir = settings.BASE_DIR / 'sent_emails'
                    email_dir.mkdir(exist_ok=True)
                    
                    # สร้างไฟล์อีเมล
                    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                    email_file = email_dir / f'email_{timestamp}.txt'
                    
                    with open(email_file, 'w', encoding='utf-8') as f:
                        f.write(f"To: {', '.join(recipient_emails)}\n")
                        f.write(f"Subject: {subject}\n")
                        f.write(f"From: {settings.DEFAULT_FROM_EMAIL}\n")
                        f.write(f"Date: {datetime.datetime.now()}\n")
                        f.write("="*50 + "\n")
                        f.write(body)
                    
                    messages.info(request, f'เก็บอีเมลเป็นไฟล์แทน: {email_file.name}')
                except Exception as file_error:
                    messages.error(request, f'ไม่สามารถเก็บอีเมลได้: {str(file_error)}')
            return render(request, 'machine/send_email_done.html', {'machine': machine})
    else:
        from .forms import SendMachineEmailForm
        form = SendMachineEmailForm()
    return render(request, 'machine/send_email.html', {'form': form, 'machine': machine})

@login_required
def calibration_data(request, pk):
    """บันทึกการสอบเทียบ - redirect ไปยังระบบการสอบเทียบใหม่"""
    machine = get_object_or_404(Machine, pk=pk)
    return redirect('machine-calibration-list', machine_id=pk)

@login_required
def send_filtered_email(request):
    """ส่งอีเมลข้อมูลเครื่องมือที่กรองแล้ว (แยกตามหน่วยงาน)"""
    if request.method == 'POST':
        # --- กรอง queryset ---
        queryset = Machine.objects.filter(deleted=False)
        if request.POST.get('organize_id'):
            queryset = queryset.filter(organize_id=request.POST['organize_id'])
        if request.POST.get('machine_type'):
            queryset = queryset.filter(machine_type_id=request.POST['machine_type'])
        if request.POST.get('date_from'):
            queryset = queryset.filter(update__gte=request.POST['date_from'])
        if request.POST.get('date_to'):
            queryset = queryset.filter(update__lte=request.POST['date_to'])
        if request.POST.get('serial_search'):
            queryset = queryset.filter(serial_number__icontains=request.POST['serial_search'])
        if request.POST.get('name_search'):
            queryset = queryset.filter(name__icontains=request.POST['name_search'])

        # --- จัดกลุ่มตามหน่วยงาน ---
        machines_by_org = {}
        for machine in queryset:
            if machine.organize and machine.organize.email:
                org_email = machine.organize.email
                if org_email not in machines_by_org:
                    machines_by_org[org_email] = {
                        "org_name": machine.organize.name,
                        "machines": []
                    }
                machines_by_org[org_email]["machines"].append(machine)

        if not machines_by_org:
            messages.warning(request, "ไม่พบหน่วยงานที่มีอีเมล")
            return redirect("machine-list")

        success_list, fail_list = [], []

        # --- ส่งเมลแยกตามหน่วยงาน ---
        for org_email, data in machines_by_org.items():
            subject = f"รายงานเครื่องมือวัดของ {data['org_name']} ({len(data['machines'])} รายการ)"
            body = f"หน่วยงาน: {data['org_name']}\n\n"

            for machine in data["machines"]:
                body += f"ID: {machine.id}\n"
                body += f"ชื่อเครื่องมือ: {machine.name}\n"
                body += f"รุ่น: {machine.model or '-'}\n"
                body += f"Serial Number: {machine.serial_number or '-'}\n"
                body += f"ประเภท: {machine.machine_type}\n"
                body += f"ผู้ผลิต: {machine.manufacture or '-'}\n"
                body += f"วันที่อัปเดต: {machine.update}\n"
                body += "-" * 50 + "\n"

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [org_email],   # ✅ ส่งแยกไปทีละเมล
                    fail_silently=False,
                )
                success_list.append(org_email)
            except Exception as e:
                fail_list.append(f"{org_email} ({str(e)})")

        # --- สรุปผล ---
        if success_list:
            messages.success(request, f"ส่งอีเมลสำเร็จไปยัง: {', '.join(success_list)}")
        if fail_list:
            messages.warning(request, f"ส่งไม่สำเร็จ: {', '.join(fail_list)}")

    return redirect("machine-list")

@login_required
def create_calibration_request(request, pk):
    """สร้างคำร้องขอบันทึกสอบเทียบสำหรับเครื่องมือ"""
    machine = get_object_or_404(Machine, id=pk)
    
    # รับ priority จาก URL parameter
    priority = request.GET.get('priority', 'normal')
    
    # ตรวจสอบประเภทเครื่องมือ
    machine_type_name = machine.machine_type.name.lower()
    
    try:
        # สร้างบันทึกการสอบเทียบตามประเภทเครื่องมือ
        if 'pressure' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = CalibrationPressure.objects.filter(
                uuc_id=machine,
                status='pending'
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = CalibrationPressure.objects.create(
                uuc_id=machine,
                status='pending',
                priority=priority
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        elif 'torque' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = CalibrationTorque.objects.filter(
                uuc_id=machine,
                status__in=['pending', 'not_set']
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = CalibrationTorque.objects.create(
                uuc_id=machine,
                status='not_set',
                priority=priority
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        elif 'balance' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = BalanceCalibration.objects.filter(
                machine=machine,
                status='pending'
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = BalanceCalibration.objects.create(
                machine=machine,
                status='pending',
                priority=priority,
                date_calibration=timezone.now().date()  # กำหนดวันที่สอบเทียบเป็นวันนี้
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        elif 'microwave' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = MicrowaveCalibration.objects.filter(
                machine=machine,
                status='pending'
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = MicrowaveCalibration.objects.create(
                machine=machine,
                status='pending',
                priority=priority,
                date_calibration=timezone.now().date()
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        elif 'high frequency' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = HighFrequencyCalibration.objects.filter(
                machine=machine,
                status='pending'
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = HighFrequencyCalibration.objects.create(
                machine=machine,
                status='pending',
                priority=priority,
                date_calibration=timezone.now().date()
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        elif 'low frequency' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = LowFrequencyCalibration.objects.filter(
                machine=machine,
                status='pending'
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = LowFrequencyCalibration.objects.create(
                machine=machine,
                status='pending',
                priority=priority,
                date_calibration=timezone.now().date()
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        elif 'dial gauge' in machine_type_name:
            # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
            existing_request = DialGaugeCalibration.objects.filter(
                machine=machine,
                status='pending'
            ).first()
            
            if existing_request:
                messages.warning(request, f'มีคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} อยู่แล้ว')
                return redirect('machine-list')
            
            # สร้างคำร้องขอใหม่
            calibration = DialGaugeCalibration.objects.create(
                machine=machine,
                status='pending',
                priority=priority,
                date_calibration=timezone.now().date()
            )
            messages.success(request, f'ส่งคำร้องขอบันทึกสอบเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            
        else:
            messages.error(request, 'ไม่พบประเภทการสอบเทียบที่เหมาะสมสำหรับเครื่องมือนี้')
            return redirect('machine-list')
        
        return redirect('machine-list')
        
    except Exception as e:
        messages.error(request, f'เกิดข้อผิดพลาดในการส่งคำร้องขอ: {str(e)}')
        return redirect('machine-list')

# CalibrationEquipment Views
class CalibrationEquipmentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CalibrationEquipment
    template_name = 'machine/calibration_equipment_list.html'
    context_object_name = 'calibration_equipment'
    permission_required = 'view_equipment'
    
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
    permission_required = 'manage_equipment'

class CalibrationEquipmentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CalibrationEquipment
    form_class = CalibrationEquipmentForm
    template_name = 'machine/calibration_equipment_form.html'
    success_url = reverse_lazy('calibration-equipment-list')
    permission_required = 'manage_equipment'

class CalibrationEquipmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CalibrationEquipment
    template_name = 'machine/calibration_equipment_confirm_delete.html'
    success_url = reverse_lazy('calibration-equipment-list')
    permission_required = 'manage_equipment'

@login_required
@require_http_methods(["POST"])
def bulk_calibration_request(request):
    """สร้างคำร้องขอบันทึกสอบเทียบสำหรับเครื่องมือหลายตัว"""
    try:
        # รับข้อมูลจาก request
        machine_ids = request.POST.getlist('machine_ids')
        priority = request.POST.get('priority', 'normal')
        
        if not machine_ids:
            return JsonResponse({
                'success': False,
                'message': 'ไม่พบเครื่องมือที่เลือก'
            })
        
        created_count = 0
        skipped_count = 0
        error_messages = []
        
        # ประมวลผลแต่ละเครื่องมือ
        for machine_id in machine_ids:
            try:
                machine = get_object_or_404(Machine, id=machine_id)
                machine_type_name = machine.machine_type.name.lower()
                
                # ตรวจสอบประเภทเครื่องมือและสร้างคำร้องขอ
                if 'pressure' in machine_type_name:
                    # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
                    existing_request = CalibrationPressure.objects.filter(
                        uuc_id=machine,
                        status='pending'
                    ).first()
                    
                    if existing_request:
                        skipped_count += 1
                        continue
                    
                    # สร้างคำร้องขอใหม่
                    CalibrationPressure.objects.create(
                        uuc_id=machine,
                        status='pending',
                        priority=priority
                    )
                    created_count += 1
                    
                elif 'torque' in machine_type_name:
                    # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
                    existing_request = CalibrationTorque.objects.filter(
                        uuc_id=machine,
                        status__in=['pending', 'not_set']
                    ).first()
                    
                    if existing_request:
                        skipped_count += 1
                        continue
                    
                    # สร้างคำร้องขอใหม่
                    CalibrationTorque.objects.create(
                        uuc_id=machine,
                        status='not_set',
                        priority=priority
                    )
                    created_count += 1
                    
                elif 'balance' in machine_type_name:
                    # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
                    existing_request = BalanceCalibration.objects.filter(
                        machine=machine,
                        status='pending'
                    ).first()
                    
                    if existing_request:
                        skipped_count += 1
                        continue
                    
                    # สร้างคำร้องขอใหม่
                    BalanceCalibration.objects.create(
                        machine=machine,
                        status='pending',
                        priority=priority,
                        date_calibration=timezone.now().date()
                    )
                    created_count += 1
                    
                elif 'microwave' in machine_type_name:
                    # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
                    existing_request = MicrowaveCalibration.objects.filter(
                        machine=machine,
                        status='pending'
                    ).first()
                    
                    if existing_request:
                        skipped_count += 1
                        continue
                    
                    # สร้างคำร้องขอใหม่
                    MicrowaveCalibration.objects.create(
                        machine=machine,
                        status='pending',
                        priority=priority,
                        date_calibration=timezone.now().date()
                    )
                    created_count += 1
                    
                elif 'high frequency' in machine_type_name:
                    # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
                    existing_request = HighFrequencyCalibration.objects.filter(
                        machine=machine,
                        status='pending'
                    ).first()
                    
                    if existing_request:
                        skipped_count += 1
                        continue
                    
                    # สร้างคำร้องขอใหม่
                    HighFrequencyCalibration.objects.create(
                        machine=machine,
                        status='pending',
                        priority=priority,
                        date_calibration=timezone.now().date()
                    )
                    created_count += 1
                    
                elif 'low frequency' in machine_type_name:
                    # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
                    existing_request = LowFrequencyCalibration.objects.filter(
                        machine=machine,
                        status='pending'
                    ).first()
                    
                    if existing_request:
                        skipped_count += 1
                        continue
                    
                    # สร้างคำร้องขอใหม่
                    LowFrequencyCalibration.objects.create(
                        machine=machine,
                        status='pending',
                        priority=priority,
                        date_calibration=timezone.now().date()
                    )
                    created_count += 1
                    
                elif 'dial gauge' in machine_type_name:
                    # ตรวจสอบว่ามีคำร้องขออยู่แล้วหรือไม่
                    existing_request = DialGaugeCalibration.objects.filter(
                        machine=machine,
                        status='pending'
                    ).first()
                    
                    if existing_request:
                        skipped_count += 1
                        continue
                    
                    # สร้างคำร้องขอใหม่
                    DialGaugeCalibration.objects.create(
                        machine=machine,
                        status='pending',
                        priority=priority,
                        date_calibration=timezone.now().date()
                    )
                    created_count += 1
                    
                else:
                    error_messages.append(f'ไม่พบประเภทการสอบเทียบที่เหมาะสมสำหรับ {machine.name}')
                    
            except Exception as e:
                error_messages.append(f'เกิดข้อผิดพลาดกับเครื่องมือ ID {machine_id}: {str(e)}')
        
        # สร้างข้อความตอบกลับ
        message = f'สร้างคำร้องขอสำเร็จ {created_count} รายการ'
        if skipped_count > 0:
            message += f', ข้าม {skipped_count} รายการที่มีคำร้องขออยู่แล้ว'
        if error_messages:
            message += f', เกิดข้อผิดพลาด {len(error_messages)} รายการ'
        
        return JsonResponse({
            'success': True,
            'created_count': created_count,
            'skipped_count': skipped_count,
            'error_count': len(error_messages),
            'message': message,
            'errors': error_messages
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'เกิดข้อผิดพลาดในการประมวลผล: {str(e)}'
        })

def _send_email_with_retry(email, max_attempts=3, delay=5):
    """ส่งอีเมลพร้อม retry mechanism"""
    import time
    import logging
    
    logger = logging.getLogger(__name__)
    
    for attempt in range(max_attempts):
        try:
            logger.info(f"Attempting to send email (attempt {attempt + 1}/{max_attempts})")
            email.send()
            logger.info("Email sent successfully")
            return True
        except Exception as e:
            logger.warning(f"Email send attempt {attempt + 1} failed: {str(e)}")
            if attempt < max_attempts - 1:
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logger.error(f"All email send attempts failed: {str(e)}")
                raise e

@login_required
def debug_user_organizations(request):
    """Debug function to check user organizations and emails"""
    import logging
    logger = logging.getLogger(__name__)
    
    user = request.user
    debug_info = {
        'username': user.username,
        'main_organization': None,
        'additional_organizations': [],
        'all_emails': []
    }
    
    # ตรวจสอบหน่วยงานหลัก
    if user.organize:
        debug_info['main_organization'] = {
            'name': user.organize.name,
            'email': user.organize.email
        }
        if user.organize.email:
            debug_info['all_emails'].append(user.organize.email)
    
    # ตรวจสอบหน่วยงานเพิ่มเติม
    for org in user.organizations.all():
        org_info = {
            'name': org.name,
            'email': org.email
        }
        debug_info['additional_organizations'].append(org_info)
        if org.email and org.email not in debug_info['all_emails']:
            debug_info['all_emails'].append(org.email)
    
    logger.info(f"Debug info: {debug_info}")
    
    return JsonResponse(debug_info)

@login_required
@require_http_methods(["POST"])
def bulk_send_email(request):
    """ส่งอีเมลข้อมูลเครื่องมือหลายตัว (แยกตามหน่วยงานของเครื่องมือ)"""
    try:
        machine_ids = request.POST.getlist('machine_ids')
        msg = request.POST.get('msg', '')

        if not machine_ids:
            return JsonResponse({
                'success': False,
                'msg': 'ไม่พบเครื่องมือที่เลือก'
            })

        machines = Machine.objects.filter(id__in=machine_ids, deleted=False)

        if not machines.exists():
            return JsonResponse({
                'success': False,
                'msg': 'ไม่พบเครื่องมือที่ถูกต้อง'
            })

        # --- จัดกลุ่มตามหน่วยงาน ---
        machines_by_org = {}
        for machine in machines:
            if machine.organize and machine.organize.email:
                org_email = machine.organize.email
                if org_email not in machines_by_org:
                    machines_by_org[org_email] = {
                        "org_name": machine.organize.name,
                        "machines": []
                    }
                machines_by_org[org_email]["machines"].append(machine)

        if not machines_by_org:
            return JsonResponse({
                'success': False,
                'msg': 'ไม่พบหน่วยงานที่มีอีเมล'
            })

        success_list, fail_list = [], []

        # --- ส่งเมลแยกตามหน่วยงาน ---
        for org_email, data in machines_by_org.items():
            subject = f"ข้อมูลเครื่องมือวัดของ {data['org_name']} ({len(data['machines'])} รายการ)"
            body = f"หน่วยงาน: {data['org_name']}\n\n"

            for machine in data["machines"]:
                body += f"ID: {machine.id}\n"
                body += f"ชื่อเครื่องมือ: {machine.name}\n"
                body += f"รุ่น: {machine.model or '-'}\n"
                body += f"Serial Number: {machine.serial_number or '-'}\n"
                body += f"ประเภท: {machine.machine_type}\n"
                body += f"ผู้ผลิต: {machine.manufacture or '-'}\n"
                body += f"ช่วงการวัด: {machine.range or '-'}\n"
                body += f"ความละเอียด: {machine.res_uuc or '-'}\n"
                body += f"วันที่อัปเดต: {machine.update}\n"
                body += "-" * 50 + "\n"

            if msg.strip():
                body += f"\nข้อความเพิ่มเติม:\n{msg}\n"

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [org_email],  # ✅ ส่งแยกทีละหน่วยงาน
                    fail_silently=False,
                )
                success_list.append(org_email)
            except Exception as e:
                fail_list.append(f"{org_email} ({str(e)})")

        # --- สรุปผล ---
        msg = ""
        if success_list:
            msg += f"ส่งอีเมลสำเร็จไปยัง: {', '.join(success_list)}. "
        if fail_list:
            msg += f"ส่งไม่สำเร็จ: {', '.join(fail_list)}"

        return JsonResponse({
            'success': True if success_list else False,
            'message': msg.strip()
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'เกิดข้อผิดพลาดในการประมวลผล: {str(e)}'
        })
