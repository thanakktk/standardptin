from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import CalibrationForce, CalibrationPressure, CalibrationTorque
from .forms import CalibrationForceForm, CalibrationPressureForm, CalibrationTorqueForm
from machine.models import Machine, MachineType
from django.db import models
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.shared import OxmlElement, qn
from datetime import datetime
import io
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

class CalibrationForceListView(LoginRequiredMixin, ListView):
    model = CalibrationForce
    template_name = 'calibrate/force_list.html'
    context_object_name = 'calibrations'

class CalibrationForceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CalibrationForce
    form_class = CalibrationForceForm
    template_name = 'calibrate/force_form.html'
    success_url = reverse_lazy('calibrate-force-list')
    permission_required = 'calibrate.add_calibrationforce'

class CalibrationForceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CalibrationForce
    form_class = CalibrationForceForm
    template_name = 'calibrate/force_form.html'
    success_url = reverse_lazy('calibrate-force-list')
    permission_required = 'calibrate.change_calibrationforce'

class CalibrationForceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CalibrationForce
    template_name = 'calibrate/force_confirm_delete.html'
    success_url = reverse_lazy('calibrate-force-list')
    permission_required = 'calibrate.delete_calibrationforce'

class CalibrationPressureListView(LoginRequiredMixin, ListView):
    model = CalibrationPressure
    template_name = 'calibrate/pressure_list.html'
    context_object_name = 'calibrations'

class CalibrationPressureCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CalibrationPressure
    form_class = CalibrationPressureForm
    template_name = 'calibrate/pressure_form.html'
    success_url = reverse_lazy('calibrate-pressure-list')
    permission_required = 'calibrate.add_calibrationpressure'

class CalibrationPressureUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CalibrationPressure
    form_class = CalibrationPressureForm
    template_name = 'calibrate/pressure_form.html'
    success_url = reverse_lazy('calibrate-pressure-list')
    permission_required = 'calibrate.change_calibrationpressure'

class CalibrationPressureDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CalibrationPressure
    template_name = 'calibrate/pressure_confirm_delete.html'
    success_url = reverse_lazy('calibrate-pressure-list')
    permission_required = 'calibrate.delete_calibrationpressure'

class CalibrationTorqueListView(LoginRequiredMixin, ListView):
    model = CalibrationTorque
    template_name = 'calibrate/torque_list.html'
    context_object_name = 'calibrations'

class CalibrationTorqueCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CalibrationTorque
    form_class = CalibrationTorqueForm
    template_name = 'calibrate/torque_form.html'
    success_url = reverse_lazy('calibrate-torque-list')
    permission_required = 'calibrate.add_calibrationtorque'

class CalibrationTorqueUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CalibrationTorque
    form_class = CalibrationTorqueForm
    template_name = 'calibrate/torque_form.html'
    success_url = reverse_lazy('calibrate-torque-list')
    permission_required = 'calibrate.change_calibrationtorque'

class CalibrationTorqueDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CalibrationTorque
    template_name = 'calibrate/torque_confirm_delete.html'
    success_url = reverse_lazy('calibrate-torque-list')
    permission_required = 'calibrate.delete_calibrationtorque'

@login_required
def calibration_dashboard(request):
    """หน้าหลักสำหรับเลือกประเภทการปรับเทียบ"""
    from datetime import date, timedelta
    
    # ดึงข้อมูลการปรับเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id').all()
    
    # รวมข้อมูลการปรับเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การปรับเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,  # ใช้ update date แทน
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การปรับเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,  # ใช้ update date แทน
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การปรับเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,  # ใช้ update date แทน
        })
    
    # เรียงลำดับตามวันที่ปรับเทียบล่าสุด
    all_calibrations.sort(key=lambda x: x['created_at'] if x['created_at'] else date.min, reverse=True)
    
    # ข้อมูลวันที่สำหรับการคำนวณสถานะ
    today = date.today()
    today_plus_30 = today + timedelta(days=30)
    
    context = {
        'force_machines': Machine.objects.filter(machine_type__name__icontains='force').count(),
        'pressure_machines': Machine.objects.filter(machine_type__name__icontains='pressure').count(),
        'torque_machines': Machine.objects.filter(machine_type__name__icontains='torque').count(),
        'total_calibrations': (
            CalibrationForce.objects.count() +
            CalibrationPressure.objects.count() +
            CalibrationTorque.objects.count()
        ),
        'all_calibrations': all_calibrations,
        'today': today,
        'today_plus_30': today_plus_30,
    }
    return render(request, 'calibrate/dashboard.html', context)

@login_required
def machine_calibration_list(request, machine_id):
    """แสดงรายการการปรับเทียบของเครื่องมือเฉพาะ"""
    machine = get_object_or_404(Machine, id=machine_id)
    
    # ตรวจสอบประเภทเครื่องมือและดึงข้อมูลการปรับเทียบที่เหมาะสม
    machine_type_name = machine.machine_type.name.lower()
    
    if 'force' in machine_type_name:
        calibrations = CalibrationForce.objects.filter(uuc_id=machine.id)
        calibration_type = 'force'
    elif 'pressure' in machine_type_name:
        calibrations = CalibrationPressure.objects.filter(uuc_id=machine.id)
        calibration_type = 'pressure'
    elif 'torque' in machine_type_name:
        calibrations = CalibrationTorque.objects.filter(uuc_id=machine.id)
        calibration_type = 'torque'
    else:
        calibrations = []
        calibration_type = 'unknown'
    
    context = {
        'machine': machine,
        'calibrations': calibrations,
        'calibration_type': calibration_type,
    }
    return render(request, 'calibrate/machine_calibration_list.html', context)

@login_required
def create_calibration_for_machine(request, machine_id):
    """สร้างบันทึกการปรับเทียบสำหรับเครื่องมือเฉพาะ"""
    machine = get_object_or_404(Machine, id=machine_id)
    machine_type_name = machine.machine_type.name.lower()
    
    if request.method == 'POST':
        if 'force' in machine_type_name:
            form = CalibrationForceForm(request.POST)
            template = 'calibrate/force_form.html'
            success_url = reverse_lazy('machine-calibration-list', kwargs={'machine_id': machine_id})
        elif 'pressure' in machine_type_name:
            form = CalibrationPressureForm(request.POST)
            template = 'calibrate/pressure_form.html'
            success_url = reverse_lazy('machine-calibration-list', kwargs={'machine_id': machine_id})
        elif 'torque' in machine_type_name:
            form = CalibrationTorqueForm(request.POST)
            template = 'calibrate/torque_form.html'
            success_url = reverse_lazy('machine-calibration-list', kwargs={'machine_id': machine_id})
        else:
            messages.error(request, 'ไม่พบประเภทการปรับเทียบที่เหมาะสม')
            return redirect('machine-list')
        
        if form.is_valid():
            calibration = form.save(commit=False)
            calibration.uuc_id = machine.id
            calibration.save()
            messages.success(request, 'บันทึกการปรับเทียบเรียบร้อยแล้ว')
            return redirect(success_url)
    else:
        if 'force' in machine_type_name:
            form = CalibrationForceForm(initial={'uuc_id': machine.id})
            template = 'calibrate/force_form.html'
        elif 'pressure' in machine_type_name:
            form = CalibrationPressureForm(initial={'uuc_id': machine.id})
            template = 'calibrate/pressure_form.html'
        elif 'torque' in machine_type_name:
            form = CalibrationTorqueForm(initial={'uuc_id': machine.id})
            template = 'calibrate/torque_form.html'
        else:
            messages.error(request, 'ไม่พบประเภทการปรับเทียบที่เหมาะสม')
            return redirect('machine-list')
    
    context = {
        'form': form,
        'machine': machine,
        'calibration_type': machine_type_name,
    }
    return render(request, template, context)

@login_required
def calibration_by_type(request, calibration_type):
    """แสดงรายการการปรับเทียบตามประเภท"""
    if calibration_type == 'force':
        calibrations = CalibrationForce.objects.all()
        template = 'calibrate/force_list.html'
    elif calibration_type == 'pressure':
        calibrations = CalibrationPressure.objects.all()
        template = 'calibrate/pressure_list.html'
    elif calibration_type == 'torque':
        calibrations = CalibrationTorque.objects.all()
        template = 'calibrate/torque_list.html'
    else:
        messages.error(request, 'ประเภทการปรับเทียบไม่ถูกต้อง')
        return redirect('calibrate-dashboard')
    
    context = {
        'calibrations': calibrations,
        'calibration_type': calibration_type,
    }
    return render(request, template, context)

@login_required
def select_machine_for_calibration(request):
    """หน้าดึงข้อมูลเครื่องมือเพื่อบันทึกการปรับเทียบ"""
    machines = Machine.objects.filter(deleted=False).order_by('name')
    
    # กรองตามประเภท
    machine_type_filter = request.GET.get('machine_type')
    if machine_type_filter:
        machines = machines.filter(machine_type__name__icontains=machine_type_filter)
    
    # ค้นหาตามชื่อหรือ serial number
    search_query = request.GET.get('search')
    if search_query:
        machines = machines.filter(
            models.Q(name__icontains=search_query) |
            models.Q(serial_number__icontains=search_query) |
            models.Q(model__icontains=search_query)
        )
    
    context = {
        'machines': machines,
        'machine_types': MachineType.objects.all(),
        'selected_type': machine_type_filter,
        'search_query': search_query,
    }
    return render(request, 'calibrate/select_machine.html', context)

@login_required
def create_calibration_with_machine(request, machine_id):
    """สร้างบันทึกการปรับเทียบพร้อมข้อมูลเครื่องมือ"""
    machine = get_object_or_404(Machine, id=machine_id)
    machine_type_name = machine.machine_type.name.lower()
    
    if request.method == 'POST':
        if 'force' in machine_type_name:
            form = CalibrationForceForm(request.POST)
            template = 'calibrate/force_form_with_machine.html'
            success_url = reverse_lazy('calibrate-force-list')
        elif 'pressure' in machine_type_name:
            # สำหรับ Pressure ใช้การประมวลผลข้อมูลแบบพิเศษ
            return process_pressure_calibration(request, machine)
        elif 'torque' in machine_type_name:
            # สำหรับ Torque ใช้การประมวลผลข้อมูลแบบพิเศษ
            return process_torque_calibration(request, machine)
        else:
            messages.error(request, 'ไม่พบประเภทการปรับเทียบที่เหมาะสม')
            return redirect('select-machine-for-calibration')
        
        if form.is_valid():
            calibration = form.save(commit=False)
            calibration.uuc_id = machine
            
            # คำนวณวันที่ครบกำหนดถัดไป (+6 เดือน)
            from datetime import datetime, timedelta
            
            if calibration.update:
                # คำนวณ 6 เดือนจากวันที่ปรับเทียบ
                year = calibration.update.year
                month = calibration.update.month + 6
                if month > 12:
                    year += month // 12
                    month = month % 12
                    if month == 0:
                        month = 12
                
                # ใช้วันที่เดิม แต่เปลี่ยนปีและเดือน
                day = min(calibration.update.day, 28)  # ป้องกันปัญหาเดือนกุมภาพันธ์
                try:
                    calibration.next_due = datetime(year, month, day).date()
                except ValueError:
                    # ถ้าวันที่ไม่ถูกต้อง ให้ใช้วันที่ 28 ของเดือนนั้น
                    calibration.next_due = datetime(year, month, 28).date()
            else:
                # ถ้าไม่มีวันที่ปรับเทียบ ให้ใช้วันที่ปัจจุบัน + 6 เดือน
                today = datetime.now().date()
                year = today.year
                month = today.month + 6
                if month > 12:
                    year += month // 12
                    month = month % 12
                    if month == 0:
                        month = 12
                
                day = min(today.day, 28)
                try:
                    calibration.next_due = datetime(year, month, day).date()
                except ValueError:
                    calibration.next_due = datetime(year, month, 28).date()
            
            calibration.save()
            messages.success(request, f'บันทึกการปรับเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            return redirect(success_url)
    else:
        # เติมข้อมูลเริ่มต้นจากเครื่องมือ
        initial_data = {
            'uuc_id': machine,
        }
        
        if 'force' in machine_type_name:
            form = CalibrationForceForm(initial=initial_data)
            template = 'calibrate/force_form_with_machine.html'
        elif 'pressure' in machine_type_name:
            form = CalibrationPressureForm(initial=initial_data)
            template = 'calibrate/pressure_form_with_machine.html'
        elif 'torque' in machine_type_name:
            form = CalibrationTorqueForm(initial=initial_data)
            template = 'calibrate/torque_form_with_machine.html'
        else:
            messages.error(request, 'ไม่พบประเภทการปรับเทียบที่เหมาะสม')
            return redirect('select-machine-for-calibration')
    
    context = {
        'form': form,
        'machine': machine,
        'calibration_type': machine_type_name,
    }
    return render(request, template, context)

@login_required
def process_torque_calibration(request, machine):
    """ประมวลผลข้อมูลการปรับเทียบ Torque"""
    if request.method == 'POST':
        try:
            print("=== DEBUG: เริ่มประมวลผลข้อมูล Torque ===")
            print(f"Machine ID: {machine.id}")
            print(f"Machine Name: {machine.name}")
            
            # สร้าง CalibrationTorque object
            calibration = CalibrationTorque()
            calibration.uuc_id = machine
            
            # ฟังก์ชันช่วยแปลงข้อมูล
            def safe_float(value, default=0.0):
                if value == '' or value is None:
                    return default
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return default
            
            # ข้อมูล CW (Clockwise) - แถวที่ 1
            cwset_1 = safe_float(request.POST.get('cwset_1', 0))
            cw0_1 = safe_float(request.POST.get('cw0_1', 0))
            cw90_1 = safe_float(request.POST.get('cw90_1', 0))
            cw180_1 = safe_float(request.POST.get('cw180_1', 0))
            cw270_1 = safe_float(request.POST.get('cw270_1', 0))
            cw_avg_1 = safe_float(request.POST.get('cw_avg_1', 0))
            cw_error_1 = safe_float(request.POST.get('cw_error_1', 0))
            cw_reading_1 = safe_float(request.POST.get('cw_reading_1', 0))
            cw_tolerance_1 = request.POST.get('cw_tolerance_1', '')
            
            print(f"CW Set: {cwset_1}")
            print(f"CW 0: {cw0_1}")
            print(f"CW 90: {cw90_1}")
            print(f"CW 180: {cw180_1}")
            print(f"CW 270: {cw270_1}")
            print(f"CW Avg: {cw_avg_1}")
            print(f"CW Error: {cw_error_1}")
            print(f"CW Reading: {cw_reading_1}")
            print(f"CW Tolerance: {cw_tolerance_1}")
            
            calibration.cwset = cwset_1
            calibration.cw0 = cw0_1
            calibration.cw90 = cw90_1
            calibration.cw180 = cw180_1
            calibration.cw270 = cw270_1
            calibration.cw_avg = cw_avg_1
            calibration.cw_error = cw_error_1
            calibration.cw_reading = cw_reading_1
            
            # แยก tolerance string เป็น start และ end
            if ' - ' in cw_tolerance_1:
                cw_parts = cw_tolerance_1.split(' - ')
                calibration.cw_tolerance_start = safe_float(cw_parts[0]) if cw_parts[0] else None
                calibration.cw_tolerance_end = safe_float(cw_parts[1]) if cw_parts[1] else None
            
            # ข้อมูล CCW (Counter-Clockwise) - แถวที่ 1
            ccwset_1 = safe_float(request.POST.get('ccwset_1', 0))
            ccw0_1 = safe_float(request.POST.get('ccw0_1', 0))
            ccw90_1 = safe_float(request.POST.get('ccw90_1', 0))
            ccw180_1 = safe_float(request.POST.get('ccw180_1', 0))
            ccw270_1 = safe_float(request.POST.get('ccw270_1', 0))
            ccw_avg_1 = safe_float(request.POST.get('ccw_avg_1', 0))
            ccw_error_1 = safe_float(request.POST.get('ccw_error_1', 0))
            ccw_reading_1 = safe_float(request.POST.get('ccw_reading_1', 0))
            ccw_tolerance_1 = request.POST.get('ccw_tolerance_1', '')
            
            print(f"CCW Set: {ccwset_1}")
            print(f"CCW 0: {ccw0_1}")
            print(f"CCW 90: {ccw90_1}")
            print(f"CCW 180: {ccw180_1}")
            print(f"CCW 270: {ccw270_1}")
            print(f"CCW Avg: {ccw_avg_1}")
            print(f"CCW Error: {ccw_error_1}")
            print(f"CCW Reading: {ccw_reading_1}")
            print(f"CCW Tolerance: {ccw_tolerance_1}")
            
            calibration.ccwset = ccwset_1
            calibration.ccw0 = ccw0_1
            calibration.ccw90 = ccw90_1
            calibration.ccw180 = ccw180_1
            calibration.ccw270 = ccw270_1
            calibration.ccw_avg = ccw_avg_1
            calibration.ccw_error = ccw_error_1
            calibration.ccw_reading = ccw_reading_1
            
            # แยก tolerance string เป็น start และ end
            if ' - ' in ccw_tolerance_1:
                ccw_parts = ccw_tolerance_1.split(' - ')
                calibration.ccw_tolerance_start = safe_float(ccw_parts[0]) if ccw_parts[0] else None
                calibration.ccw_tolerance_end = safe_float(ccw_parts[1]) if ccw_parts[1] else None
            
            # วันที่ปรับเทียบ
            update_date = request.POST.get('update')
            if update_date:
                calibration.update = update_date
                print(f"Update Date: {update_date}")
            
            # คำนวณวันที่ครบกำหนดถัดไป (+6 เดือน)
            from datetime import datetime, timedelta
            
            if calibration.update:
                # แปลง string เป็น date object
                try:
                    update_date_obj = datetime.strptime(calibration.update, '%Y-%m-%d').date()
                    # คำนวณ 6 เดือนจากวันที่ปรับเทียบ
                    year = update_date_obj.year
                    month = update_date_obj.month + 6
                    if month > 12:
                        year += month // 12
                        month = month % 12
                        if month == 0:
                            month = 12
                    
                    # ใช้วันที่เดิม แต่เปลี่ยนปีและเดือน
                    day = min(update_date_obj.day, 28)  # ป้องกันปัญหาเดือนกุมภาพันธ์
                    try:
                        calibration.next_due = datetime(year, month, day).date()
                    except ValueError:
                        # ถ้าวันที่ไม่ถูกต้อง ให้ใช้วันที่ 28 ของเดือนนั้น
                        calibration.next_due = datetime(year, month, 28).date()
                    print(f"Next Due Date: {calibration.next_due}")
                except ValueError as e:
                    print(f"Error parsing date: {e}")
                    # ถ้าแปลงวันที่ไม่ได้ ให้ใช้วันที่ปัจจุบัน + 6 เดือน
                    today = datetime.now().date()
                    year = today.year
                    month = today.month + 6
                    if month > 12:
                        year += month // 12
                        month = month % 12
                        if month == 0:
                            month = 12
                    
                    day = min(today.day, 28)
                    try:
                        calibration.next_due = datetime(year, month, day).date()
                    except ValueError:
                        calibration.next_due = datetime(year, month, 28).date()
                    print(f"Next Due Date (default): {calibration.next_due}")
            else:
                # ถ้าไม่มีวันที่ปรับเทียบ ให้ใช้วันที่ปัจจุบัน + 6 เดือน
                today = datetime.now().date()
                year = today.year
                month = today.month + 6
                if month > 12:
                    year += month // 12
                    month = month % 12
                    if month == 0:
                        month = 12
                
                day = min(today.day, 28)
                try:
                    calibration.next_due = datetime(year, month, day).date()
                except ValueError:
                    calibration.next_due = datetime(year, month, 28).date()
                print(f"Next Due Date (default): {calibration.next_due}")
            
            print("=== DEBUG: บันทึกข้อมูล ===")
            calibration.save()
            print(f"บันทึกสำเร็จ! ID: {calibration.cal_torque_id}")
            
            messages.success(request, f'บันทึกการปรับเทียบ Torque สำหรับ {machine.name} เรียบร้อยแล้ว')
            return redirect('calibrate-torque-list')
            
        except Exception as e:
            print(f"=== DEBUG: เกิดข้อผิดพลาด ===")
            print(f"Error: {str(e)}")
            import traceback
            traceback.print_exc()
            messages.error(request, f'เกิดข้อผิดพลาดในการบันทึกข้อมูล: {str(e)}')
            return redirect('select-machine-for-calibration')
    
    # ถ้าไม่ใช่ POST request
    messages.error(request, 'วิธีการส่งข้อมูลไม่ถูกต้อง')
    return redirect('select-machine-for-calibration')

@login_required
def process_pressure_calibration(request, machine):
    """ประมวลผลข้อมูลการปรับเทียบ Pressure"""
    if request.method == 'POST':
        try:
            print("=== DEBUG: เริ่มประมวลผลข้อมูล Pressure ===")
            print(f"Machine ID: {machine.id}")
            print(f"Machine Name: {machine.name}")
            
            # สร้าง CalibrationPressure object
            calibration = CalibrationPressure()
            calibration.uuc_id = machine
            
            # ฟังก์ชันช่วยแปลงข้อมูล
            def safe_float(value, default=0.0):
                if value == '' or value is None:
                    return default
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return default
            
            # ข้อมูลจากแถวที่ 1
            set_1 = safe_float(request.POST.get('set_1', 0))
            m1_1 = safe_float(request.POST.get('m1_1', 0))
            m2_1 = safe_float(request.POST.get('m2_1', 0))
            m3_1 = safe_float(request.POST.get('m3_1', 0))
            m4_1 = safe_float(request.POST.get('m4_1', 0))
            avg_1 = safe_float(request.POST.get('avg_1', 0))
            error_1 = safe_float(request.POST.get('error_1', 0))
            tolerance_1 = request.POST.get('tolerance_1', '')
            
            print(f"Set: {set_1}")
            print(f"M1: {m1_1}")
            print(f"M2: {m2_1}")
            print(f"M3: {m3_1}")
            print(f"M4: {m4_1}")
            print(f"AVG: {avg_1}")
            print(f"Error: {error_1}")
            print(f"Tolerance: {tolerance_1}")
            
            # ใช้ข้อมูลจากแถวแรกเป็นหลัก
            calibration.set = str(set_1) if set_1 != 0 else ''
            calibration.m1 = str(m1_1) if m1_1 != 0 else ''
            calibration.m2 = str(m2_1) if m2_1 != 0 else ''
            calibration.m3 = str(m3_1) if m3_1 != 0 else ''
            calibration.m4 = str(m4_1) if m4_1 != 0 else ''
            calibration.avg = avg_1
            calibration.error = error_1
            
            # แยก tolerance string เป็น start และ end
            if ' - ' in tolerance_1:
                tolerance_parts = tolerance_1.split(' - ')
                calibration.tolerance_start = safe_float(tolerance_parts[0]) if tolerance_parts[0] else None
                calibration.tolerance_end = safe_float(tolerance_parts[1]) if tolerance_parts[1] else None
            
            # ข้อมูลทั่วไป
            update_date = request.POST.get('update')
            if update_date:
                calibration.update = update_date
                print(f"Update Date: {update_date}")
            
            # คำนวณวันที่ครบกำหนดถัดไป (+6 เดือน)
            from datetime import datetime, timedelta
            
            if calibration.update:
                # แปลง string เป็น date object
                try:
                    update_date_obj = datetime.strptime(calibration.update, '%Y-%m-%d').date()
                    # คำนวณ 6 เดือนจากวันที่ปรับเทียบ
                    year = update_date_obj.year
                    month = update_date_obj.month + 6
                    if month > 12:
                        year += month // 12
                        month = month % 12
                        if month == 0:
                            month = 12
                    
                    # ใช้วันที่เดิม แต่เปลี่ยนปีและเดือน
                    day = min(update_date_obj.day, 28)  # ป้องกันปัญหาเดือนกุมภาพันธ์
                    try:
                        calibration.next_due = datetime(year, month, day).date()
                    except ValueError:
                        # ถ้าวันที่ไม่ถูกต้อง ให้ใช้วันที่ 28 ของเดือนนั้น
                        calibration.next_due = datetime(year, month, 28).date()
                    print(f"Next Due Date: {calibration.next_due}")
                except ValueError as e:
                    print(f"Error parsing date: {e}")
                    # ถ้าแปลงวันที่ไม่ได้ ให้ใช้วันที่ปัจจุบัน + 6 เดือน
                    today = datetime.now().date()
                    year = today.year
                    month = today.month + 6
                    if month > 12:
                        year += month // 12
                        month = month % 12
                        if month == 0:
                            month = 12
                    
                    day = min(today.day, 28)
                    try:
                        calibration.next_due = datetime(year, month, day).date()
                    except ValueError:
                        calibration.next_due = datetime(year, month, 28).date()
                    print(f"Next Due Date (default): {calibration.next_due}")
            else:
                # ถ้าไม่มีวันที่ปรับเทียบ ให้ใช้วันที่ปัจจุบัน + 6 เดือน
                today = datetime.now().date()
                year = today.year
                month = today.month + 6
                if month > 12:
                    year += month // 12
                    month = month % 12
                    if month == 0:
                        month = 12
                
                day = min(today.day, 28)
                try:
                    calibration.next_due = datetime(year, month, day).date()
                except ValueError:
                    calibration.next_due = datetime(year, month, 28).date()
                print(f"Next Due Date (default): {calibration.next_due}")
            
            # ข้อมูลเพิ่มเติม
            status = request.POST.get('status', 'not_set')
            priority = request.POST.get('priority', 'normal')
            std_id = request.POST.get('std_id')
            
            calibration.status = status
            calibration.priority = priority
            if std_id and std_id != '':
                calibration.std_id_id = int(std_id)
            
            print("=== DEBUG: บันทึกข้อมูล ===")
            calibration.save()
            print(f"บันทึกสำเร็จ! ID: {calibration.cal_pressure_id}")
            
            messages.success(request, f'บันทึกการปรับเทียบ Pressure สำหรับ {machine.name} เรียบร้อยแล้ว')
            return redirect('calibrate-pressure-list')
            
        except Exception as e:
            print(f"=== DEBUG: เกิดข้อผิดพลาด ===")
            print(f"Error: {str(e)}")
            import traceback
            traceback.print_exc()
            messages.error(request, f'เกิดข้อผิดพลาดในการบันทึกข้อมูล: {str(e)}')
            return redirect('select-machine-for-calibration')
    
    # ถ้าไม่ใช่ POST request
    messages.error(request, 'วิธีการส่งข้อมูลไม่ถูกต้อง')
    return redirect('select-machine-for-calibration')

@login_required
def calibration_report(request):
    """หน้ารายงานปรับเทียบ"""
    from datetime import date, timedelta
    
    # ดึงข้อมูลการปรับเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id').all()
    
    # รวมข้อมูลการปรับเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การปรับเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,  # ใช้ update date แทน
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การปรับเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,  # ใช้ update date แทน
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การปรับเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,  # ใช้ update date แทน
        })
    
    # เรียงลำดับตามวันที่ปรับเทียบล่าสุด
    all_calibrations.sort(key=lambda x: x['created_at'] if x['created_at'] else date.min, reverse=True)
    
    # ข้อมูลวันที่สำหรับการคำนวณสถานะ
    today = date.today()
    today_plus_30 = today + timedelta(days=30)
    
    context = {
        'force_machines': Machine.objects.filter(machine_type__name__icontains='force').count(),
        'pressure_machines': Machine.objects.filter(machine_type__name__icontains='pressure').count(),
        'torque_machines': Machine.objects.filter(machine_type__name__icontains='torque').count(),
        'total_calibrations': (
            CalibrationForce.objects.count() +
            CalibrationPressure.objects.count() +
            CalibrationTorque.objects.count()
        ),
        'all_calibrations': all_calibrations,
        'today': today,
        'today_plus_30': today_plus_30,
    }
    return render(request, 'calibrate/dashboard.html', context)

@login_required
def calibration_report_detail(request):
    """หน้ารายงานผลปรับเทียบแบบละเอียด"""
    from datetime import date, timedelta
    
    # รับพารามิเตอร์การกรอง
    department = request.GET.get('department', '')
    instrument_type = request.GET.get('instrument_type', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    serial_search = request.GET.get('serial_search', '')
    name_search = request.GET.get('name_search', '')
    status_filter = request.GET.get('status_filter', '')
    
    # ดึงข้อมูลการปรับเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id').all()
    
    # รวมข้อมูลการปรับเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การปรับเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การปรับเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การปรับเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # กรองข้อมูลตามพารามิเตอร์
    filtered_calibrations = []
    for cal in all_calibrations:
        include_item = True
        
        # กรองตาม Serial Number
        if serial_search and serial_search.lower() not in cal['serial_number'].lower():
            include_item = False
        
        # กรองตามชื่อเครื่องมือ
        if name_search and name_search.lower() not in cal['machine_name'].lower():
            include_item = False
        
        # กรองตามประเภทเครื่องมือ
        if instrument_type:
            if instrument_type == 'force' and cal['type'] != 'force':
                include_item = False
            elif instrument_type == 'pressure' and cal['type'] != 'pressure':
                include_item = False
            elif instrument_type == 'torque' and cal['type'] != 'torque':
                include_item = False
        
        # กรองตามสถานะ
        if status_filter:
            if status_filter == 'cert_issued' and cal['status'] not in ['cert_issued', 'passed', 'active']:
                include_item = False
            elif status_filter == 'failed' and cal['status'] not in ['failed', 'pending', 'in_progress', 'not_set']:
                include_item = False
        
        # กรองตามวันที่
        if start_date and cal['update_date']:
            try:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
                if cal['update_date'] < start_date_obj:
                    include_item = False
            except:
                pass
        
        if end_date and cal['update_date']:
            try:
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
                if cal['update_date'] > end_date_obj:
                    include_item = False
            except:
                pass
        
        if include_item:
            filtered_calibrations.append(cal)
    
    # เรียงลำดับตามวันที่ปรับเทียบล่าสุด
    filtered_calibrations.sort(key=lambda x: x['created_at'] if x['created_at'] else date.min, reverse=True)
    
    # ข้อมูลวันที่สำหรับการคำนวณสถานะ
    today = date.today()
    today_plus_30 = today + timedelta(days=30)
    
    context = {
        'force_machines': Machine.objects.filter(machine_type__name__icontains='force').count(),
        'pressure_machines': Machine.objects.filter(machine_type__name__icontains='pressure').count(),
        'torque_machines': Machine.objects.filter(machine_type__name__icontains='torque').count(),
        'total_calibrations': (
            CalibrationForce.objects.count() +
            CalibrationPressure.objects.count() +
            CalibrationTorque.objects.count()
        ),
        'all_calibrations': filtered_calibrations,
        'today': today,
        'today_plus_30': today_plus_30,
        # พารามิเตอร์การกรอง
        'department': department,
        'instrument_type': instrument_type,
        'start_date': start_date,
        'end_date': end_date,
        'serial_search': serial_search,
        'name_search': name_search,
        'status_filter': status_filter,
    }
    return render(request, 'calibrate/calibration_report_detail.html', context)

@login_required
def export_to_word(request):
    """Export รายงานปรับเทียบเป็นไฟล์ Word"""
    from datetime import date, timedelta
    
    # รับพารามิเตอร์การกรอง (เหมือนกับใน calibration_report_detail)
    department = request.GET.get('department', '')
    instrument_type = request.GET.get('instrument_type', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    serial_search = request.GET.get('serial_search', '')
    name_search = request.GET.get('name_search', '')
    status_filter = request.GET.get('status_filter', '')
    
    # ดึงข้อมูลการปรับเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id').all()
    
    # รวมข้อมูลการปรับเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การปรับเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การปรับเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การปรับเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # กรองข้อมูลตามพารามิเตอร์ (เหมือนกับใน calibration_report_detail)
    filtered_calibrations = []
    for cal in all_calibrations:
        include_item = True
        
        # กรองตาม Serial Number
        if serial_search and serial_search.lower() not in cal['serial_number'].lower():
            include_item = False
        
        # กรองตามชื่อเครื่องมือ
        if name_search and name_search.lower() not in cal['machine_name'].lower():
            include_item = False
        
        # กรองตามประเภทเครื่องมือ
        if instrument_type:
            if instrument_type == 'force' and cal['type'] != 'force':
                include_item = False
            elif instrument_type == 'pressure' and cal['type'] != 'pressure':
                include_item = False
            elif instrument_type == 'torque' and cal['type'] != 'torque':
                include_item = False
        
        # กรองตามสถานะ
        if status_filter:
            if status_filter == 'cert_issued' and cal['status'] not in ['cert_issued', 'passed', 'active']:
                include_item = False
            elif status_filter == 'failed' and cal['status'] not in ['failed', 'pending', 'in_progress', 'not_set']:
                include_item = False
        
        # กรองตามวันที่
        if start_date and cal['update_date']:
            try:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
                if cal['update_date'] < start_date_obj:
                    include_item = False
            except:
                pass
        
        if end_date and cal['update_date']:
            try:
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
                if cal['update_date'] > end_date_obj:
                    include_item = False
            except:
                pass
        
        if include_item:
            filtered_calibrations.append(cal)
    
    # เรียงลำดับตามวันที่ปรับเทียบล่าสุด
    filtered_calibrations.sort(key=lambda x: x['created_at'] if x['created_at'] else date.min, reverse=True)
    
    # สร้าง Word document
    doc = Document()
    
    # ตั้งค่าหน้ากระดาษ
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    
    # หัวเรื่อง
    title = doc.add_heading('รายงานปรับเทียบ', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # วันที่รายงาน
    date_paragraph = doc.add_paragraph()
    date_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    date_run = date_paragraph.add_run(f'วันที่: {datetime.now().strftime("%d/%m/%Y")}')
    date_run.font.size = Pt(12)
    
    # เพิ่มบรรทัดว่าง
    doc.add_paragraph()
    
    # สร้างตาราง
    table = doc.add_table(rows=1, cols=7)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # หัวตาราง
    header_cells = table.rows[0].cells
    headers = ['ลำดับ', 'Model', 'SERIAL No.', 'ชื่อเครื่องวัด', 'หน่วยผู้ใช้', 'จำนวน', 'หมายเหตุ']
    
    for i, header in enumerate(headers):
        header_cells[i].text = header
        header_cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        header_cells[i].paragraphs[0].runs[0].font.bold = True
    
    # เพิ่มข้อมูลในตาราง
    for i, cal in enumerate(filtered_calibrations, 1):
        row_cells = table.add_row().cells
        
        # ลำดับ
        row_cells[0].text = str(i)
        row_cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Model
        row_cells[1].text = cal['machine_model'] if cal['machine_model'] != '-' else '-'
        row_cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # SERIAL No.
        row_cells[2].text = cal['serial_number'] if cal['serial_number'] != '-' else '-'
        row_cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # ชื่อเครื่องวัด
        if cal['type'] == 'force':
            instrument_name = 'Force Gauge'
        elif cal['type'] == 'pressure':
            instrument_name = 'Pressure Gauge'
        elif cal['type'] == 'torque':
            instrument_name = 'Torque Wrench'
        else:
            instrument_name = cal['type_name']
        
        row_cells[3].text = instrument_name
        row_cells[3].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # หน่วยผู้ใช้
        row_cells[4].text = 'ฝสอ.ฝูง ๔๐๓ บน.๔'
        row_cells[4].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # จำนวน
        row_cells[5].text = '๑'
        row_cells[5].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # หมายเหตุ
        if cal['status'] in ['cert_issued', 'passed', 'active']:
            remark = 'ออกใบรับรอง'
        elif cal['status'] in ['failed', 'pending', 'in_progress', 'not_set']:
            remark = 'ไม่ผ่านการปรับเทียบ'
        else:
            remark = cal['status']
        
        row_cells[6].text = remark
        row_cells[6].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # เพิ่มบรรทัดว่าง
    doc.add_paragraph()
    
    # สรุปข้อมูล
    summary_paragraph = doc.add_paragraph()
    summary_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    summary_run = summary_paragraph.add_run(f'สรุป: รายการทั้งหมด {len(filtered_calibrations)} รายการ')
    summary_run.font.size = Pt(12)
    summary_run.font.bold = True
    
    # บันทึกไฟล์
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    
    # ส่งไฟล์กลับ
    response = HttpResponse(
        buffer.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = f'attachment; filename="รายงานปรับเทียบ_{datetime.now().strftime("%Y%m%d")}.docx"'
    
    return response

@login_required
def export_to_excel(request):
    """Export รายงานปรับเทียบเป็นไฟล์ Excel"""
    from datetime import date, timedelta
    
    # รับพารามิเตอร์การกรอง (เหมือนกับใน calibration_report_detail)
    department = request.GET.get('department', '')
    instrument_type = request.GET.get('instrument_type', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    serial_search = request.GET.get('serial_search', '')
    name_search = request.GET.get('name_search', '')
    status_filter = request.GET.get('status_filter', '')
    
    # ดึงข้อมูลการปรับเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id').all()
    
    # รวมข้อมูลการปรับเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การปรับเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การปรับเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การปรับเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'created_at': cal.update,
        })
    
    # กรองข้อมูลตามพารามิเตอร์ (เหมือนกับใน calibration_report_detail)
    filtered_calibrations = []
    for cal in all_calibrations:
        include_item = True
        
        # กรองตาม Serial Number
        if serial_search and serial_search.lower() not in cal['serial_number'].lower():
            include_item = False
        
        # กรองตามชื่อเครื่องมือ
        if name_search and name_search.lower() not in cal['machine_name'].lower():
            include_item = False
        
        # กรองตามประเภทเครื่องมือ
        if instrument_type:
            if instrument_type == 'force' and cal['type'] != 'force':
                include_item = False
            elif instrument_type == 'pressure' and cal['type'] != 'pressure':
                include_item = False
            elif instrument_type == 'torque' and cal['type'] != 'torque':
                include_item = False
        
        # กรองตามสถานะ
        if status_filter:
            if status_filter == 'cert_issued' and cal['status'] not in ['cert_issued', 'passed', 'active']:
                include_item = False
            elif status_filter == 'failed' and cal['status'] not in ['failed', 'pending', 'in_progress', 'not_set']:
                include_item = False
        
        # กรองตามวันที่
        if start_date and cal['update_date']:
            try:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
                if cal['update_date'] < start_date_obj:
                    include_item = False
            except:
                pass
        
        if end_date and cal['update_date']:
            try:
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
                if cal['update_date'] > end_date_obj:
                    include_item = False
            except:
                pass
        
        if include_item:
            filtered_calibrations.append(cal)
    
    # เรียงลำดับตามวันที่ปรับเทียบล่าสุด
    filtered_calibrations.sort(key=lambda x: x['created_at'] if x['created_at'] else date.min, reverse=True)
    
    # สร้าง Excel workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "รายงานปรับเทียบ"
    
    # ตั้งค่าหัวเรื่อง
    title_font = Font(name='TH Sarabun New', size=16, bold=True)
    header_font = Font(name='TH Sarabun New', size=12, bold=True)
    cell_font = Font(name='TH Sarabun New', size=11)
    
    # สีสำหรับ header
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    
    # หัวเรื่อง
    ws['A1'] = 'รายงานปรับเทียบ'
    ws['A1'].font = title_font
    ws.merge_cells('A1:G1')
    ws['A1'].alignment = Alignment(horizontal='center')
    
    # วันที่รายงาน
    ws['A2'] = f'วันที่: {datetime.now().strftime("%d/%m/%Y")}'
    ws['A2'].font = cell_font
    ws.merge_cells('A2:G2')
    ws['A2'].alignment = Alignment(horizontal='center')
    
    # หัวตาราง
    headers = ['ลำดับ', 'Model', 'SERIAL No.', 'ชื่อเครื่องวัด', 'หน่วยผู้ใช้', 'จำนวน', 'หมายเหตุ']
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # เพิ่มข้อมูลในตาราง
    for row, cal in enumerate(filtered_calibrations, 5):
        # ลำดับ
        ws.cell(row=row, column=1, value=row-4).alignment = Alignment(horizontal='center')
        
        # Model
        model_value = cal['machine_model'] if cal['machine_model'] != '-' else '-'
        ws.cell(row=row, column=2, value=model_value).alignment = Alignment(horizontal='center')
        
        # SERIAL No.
        serial_value = cal['serial_number'] if cal['serial_number'] != '-' else '-'
        ws.cell(row=row, column=3, value=serial_value).alignment = Alignment(horizontal='center')
        
        # ชื่อเครื่องวัด
        if cal['type'] == 'force':
            instrument_name = 'Force Gauge'
        elif cal['type'] == 'pressure':
            instrument_name = 'Pressure Gauge'
        elif cal['type'] == 'torque':
            instrument_name = 'Torque Wrench'
        else:
            instrument_name = cal['type_name']
        
        ws.cell(row=row, column=4, value=instrument_name).alignment = Alignment(horizontal='center')
        
        # หน่วยผู้ใช้
        ws.cell(row=row, column=5, value='ฝสอ.ฝูง ๔๐๓ บน.๔').alignment = Alignment(horizontal='center')
        
        # จำนวน
        ws.cell(row=row, column=6, value='๑').alignment = Alignment(horizontal='center')
        
        # หมายเหตุ
        if cal['status'] in ['cert_issued', 'passed', 'active']:
            remark = 'ออกใบรับรอง'
        elif cal['status'] in ['failed', 'pending', 'in_progress', 'not_set']:
            remark = 'ไม่ผ่านการปรับเทียบ'
        else:
            remark = cal['status']
        
        ws.cell(row=row, column=7, value=remark).alignment = Alignment(horizontal='center')
    
    # ปรับความกว้างคอลัมน์
    column_widths = [8, 15, 15, 20, 25, 10, 20]
    for col, width in enumerate(column_widths, 1):
        ws.column_dimensions[get_column_letter(col)].width = width
    
    # เพิ่มเส้นขอบ
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    for row in range(4, len(filtered_calibrations) + 5):
        for col in range(1, 8):
            ws.cell(row=row, column=col).border = thin_border
    
    # บันทึกไฟล์
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    
    # ส่งไฟล์กลับ
    response = HttpResponse(
        buffer.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="รายงานปรับเทียบ_{datetime.now().strftime("%Y%m%d")}.xlsx"'
    
    return response
