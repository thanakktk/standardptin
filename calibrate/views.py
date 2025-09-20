from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import CalibrationForce, CalibrationPressure, CalibrationTorque, DialGaugeCalibration, BalanceCalibration, MicrowaveCalibration
from .forms import CalibrationForceForm, CalibrationPressureForm, CalibrationTorqueForm, DialGaugeCalibrationForm, BalanceCalibrationForm, MicrowaveCalibrationForm
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
    
    def get_queryset(self):
        # เรียงลำดับตามระดับความเร่งด่วน: ด่วนมาก -> ด่วน -> ปกติ
        return CalibrationForce.objects.annotate(
            priority_order=models.Case(
                models.When(priority='very_urgent', then=models.Value(1)),
                models.When(priority='urgent', then=models.Value(2)),
                models.When(priority='normal', then=models.Value(3)),
                default=models.Value(4),
                output_field=models.IntegerField(),
            )
        ).order_by('priority_order', '-update')

class CalibrationForceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CalibrationForce
    form_class = CalibrationForceForm
    template_name = 'calibrate/force_form.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.add_calibrationforce'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        form.fields['calibrator'].queryset = users
        form.fields['certificate_issuer'].queryset = users
        return form

class CalibrationForceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CalibrationForce
    form_class = CalibrationForceForm
    template_name = 'calibrate/force_form.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.change_calibrationforce'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        form.fields['calibrator'].queryset = users
        form.fields['certificate_issuer'].queryset = users
        return form

class CalibrationForceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CalibrationForce
    template_name = 'calibrate/force_confirm_delete.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.delete_calibrationforce'

class CalibrationPressureListView(LoginRequiredMixin, ListView):
    model = CalibrationPressure
    template_name = 'calibrate/pressure_list.html'
    context_object_name = 'calibrations'
    
    def get_queryset(self):
        # เรียงลำดับตามระดับความเร่งด่วน: ด่วนมาก -> ด่วน -> ปกติ
        return CalibrationPressure.objects.annotate(
            priority_order=models.Case(
                models.When(priority='very_urgent', then=models.Value(1)),
                models.When(priority='urgent', then=models.Value(2)),
                models.When(priority='normal', then=models.Value(3)),
                default=models.Value(4),
                output_field=models.IntegerField(),
            )
        ).order_by('priority_order', '-update')

class CalibrationPressureCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CalibrationPressure
    form_class = CalibrationPressureForm
    template_name = 'calibrate/pressure_form.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.add_calibrationpressure'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        form.fields['calibrator'].queryset = users
        form.fields['certificate_issuer'].queryset = users
        return form

class CalibrationPressureUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CalibrationPressure
    form_class = CalibrationPressureForm
    template_name = 'calibrate/pressure_form.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.change_calibrationpressure'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        form.fields['calibrator'].queryset = users
        form.fields['certificate_issuer'].queryset = users
        return form

class CalibrationPressureDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CalibrationPressure
    template_name = 'calibrate/pressure_confirm_delete.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.delete_calibrationpressure'

class CalibrationTorqueListView(LoginRequiredMixin, ListView):
    model = CalibrationTorque
    template_name = 'calibrate/torque_list.html'
    context_object_name = 'calibrations'
    
    def get_queryset(self):
        # เรียงลำดับตามระดับความเร่งด่วน: ด่วนมาก -> ด่วน -> ปกติ
        return CalibrationTorque.objects.annotate(
            priority_order=models.Case(
                models.When(priority='very_urgent', then=models.Value(1)),
                models.When(priority='urgent', then=models.Value(2)),
                models.When(priority='normal', then=models.Value(3)),
                default=models.Value(4),
                output_field=models.IntegerField(),
            )
        ).order_by('priority_order', '-update')

class CalibrationTorqueCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CalibrationTorque
    form_class = CalibrationTorqueForm
    template_name = 'calibrate/torque_form.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.add_calibrationtorque'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        form.fields['calibrator'].queryset = users
        form.fields['certificate_issuer'].queryset = users
        return form

class CalibrationTorqueUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CalibrationTorque
    form_class = CalibrationTorqueForm
    template_name = 'calibrate/torque_form.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.change_calibrationtorque'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        form.fields['calibrator'].queryset = users
        form.fields['certificate_issuer'].queryset = users
        return form

class CalibrationTorqueDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CalibrationTorque
    template_name = 'calibrate/torque_confirm_delete.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.delete_calibrationtorque'

class BalanceCalibrationListView(LoginRequiredMixin, ListView):
    model = BalanceCalibration
    template_name = 'calibrate/balance_list.html'
    context_object_name = 'calibrations'
    
    def get_queryset(self):
        # เรียงลำดับตามระดับความเร่งด่วน: ด่วนมาก -> ด่วน -> ปกติ
        return BalanceCalibration.objects.annotate(
            priority_order=models.Case(
                models.When(priority='very_urgent', then=models.Value(1)),
                models.When(priority='urgent', then=models.Value(2)),
                models.When(priority='normal', then=models.Value(3)),
                default=models.Value(4),
                output_field=models.IntegerField(),
            )
        ).order_by('priority_order', '-date_calibration')

class BalanceCalibrationCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = BalanceCalibration
    form_class = BalanceCalibrationForm
    template_name = 'calibrate/balance_form.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.add_balancecalibration'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        form.fields['calibrator'].queryset = users
        form.fields['certificate_issuer'].queryset = users
        return form

class BalanceCalibrationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BalanceCalibration
    form_class = BalanceCalibrationForm
    template_name = 'calibrate/balance_form.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.change_balancecalibration'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        form.fields['calibrator'].queryset = users
        form.fields['certificate_issuer'].queryset = users
        return form

class BalanceCalibrationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BalanceCalibration
    template_name = 'calibrate/balance_confirm_delete.html'
    success_url = reverse_lazy('calibrate-dashboard')
    permission_required = 'calibrate.delete_balancecalibration'

@login_required
def calibration_dashboard(request):
    """หน้าหลักสำหรับเลือกประเภทการสอบเทียบ"""
    from datetime import date, timedelta
    
    # รับพารามิเตอร์การค้นหาและกรอง
    name_search = request.GET.get('name_search', '')
    serial_search = request.GET.get('serial_search', '')
    calibration_type = request.GET.get('calibration_type', '')
    status_filter = request.GET.get('status_filter', '')
    priority_filter = request.GET.get('priority_filter', '')
    
    # ดึงข้อมูลการสอบเทียบทั้งหมด (ยกเว้นงานที่ปิดแล้ว) เรียงตามระดับความเร่งด่วน
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').exclude(
        status='closed'
    ).annotate(
        priority_order=models.Case(
            models.When(priority='very_urgent', then=models.Value(1)),
            models.When(priority='urgent', then=models.Value(2)),
            models.When(priority='normal', then=models.Value(3)),
            default=models.Value(4),
            output_field=models.IntegerField(),
        )
    ).order_by('priority_order', '-update')
    
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').exclude(
        status='closed'
    ).annotate(
        priority_order=models.Case(
            models.When(priority='very_urgent', then=models.Value(1)),
            models.When(priority='urgent', then=models.Value(2)),
            models.When(priority='normal', then=models.Value(3)),
            default=models.Value(4),
            output_field=models.IntegerField(),
        )
    ).order_by('priority_order', '-update')
    
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').exclude(
        status='closed'
    ).annotate(
        priority_order=models.Case(
            models.When(priority='very_urgent', then=models.Value(1)),
            models.When(priority='urgent', then=models.Value(2)),
            models.When(priority='normal', then=models.Value(3)),
            default=models.Value(4),
            output_field=models.IntegerField(),
        )
    ).order_by('priority_order', '-update')
    
    # ดึงข้อมูลการสอบเทียบ Dial Gauge
    dial_gauge_calibrations = DialGaugeCalibration.objects.select_related('machine', 'std_id', 'calibrator', 'certificate_issuer').exclude(
        status='closed'
    ).annotate(
        priority_order=models.Case(
            models.When(priority='very_urgent', then=models.Value(1)),
            models.When(priority='urgent', then=models.Value(2)),
            models.When(priority='normal', then=models.Value(3)),
            default=models.Value(4),
            output_field=models.IntegerField(),
        )
    ).order_by('priority_order', '-date_calibration')
    
    # ดึงข้อมูลการสอบเทียบ Balance
    balance_calibrations = BalanceCalibration.objects.select_related('machine', 'std_id', 'calibrator', 'certificate_issuer').exclude(
        status='closed'
    ).annotate(
        priority_order=models.Case(
            models.When(priority='very_urgent', then=models.Value(1)),
            models.When(priority='urgent', then=models.Value(2)),
            models.When(priority='normal', then=models.Value(3)),
            default=models.Value(4),
            output_field=models.IntegerField(),
        )
    ).order_by('priority_order', '-date_calibration')
    
    # ดึงข้อมูลการสอบเทียบ Microwave
    microwave_calibrations = MicrowaveCalibration.objects.select_related('machine', 'std_id', 'calibrator', 'certificate_issuer').exclude(
        status='closed'
    ).annotate(
        priority_order=models.Case(
            models.When(priority='very_urgent', then=models.Value(1)),
            models.When(priority='urgent', then=models.Value(2)),
            models.When(priority='normal', then=models.Value(3)),
            default=models.Value(4),
            output_field=models.IntegerField(),
        )
    ).order_by('priority_order', '-date_calibration')
    
    # รวมข้อมูลการสอบเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การสอบเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การสอบเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การสอบเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Dial Gauge calibrations
    for cal in dial_gauge_calibrations:
        all_calibrations.append({
            'id': cal.id,
            'type': 'dial_gauge',
            'type_name': 'การสอบเทียบ Dial Gauge',
            'machine_name': cal.machine.name if cal.machine else '-',
            'machine_model': cal.machine.model if cal.machine else '-',
            'serial_number': cal.machine.serial_number if cal.machine else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.date_calibration,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Balance calibrations
    for cal in balance_calibrations:
        all_calibrations.append({
            'id': cal.id,
            'type': 'balance',
            'type_name': 'การสอบเทียบ Balance',
            'machine_name': cal.machine.name if cal.machine else '-',
            'machine_model': cal.machine.model if cal.machine else '-',
            'serial_number': cal.machine.serial_number if cal.machine else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.date_calibration,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Microwave calibrations
    for cal in microwave_calibrations:
        all_calibrations.append({
            'id': cal.id,
            'type': 'microwave',
            'type_name': 'การสอบเทียบ Microwave',
            'machine_name': cal.machine.name if cal.machine else '-',
            'machine_model': cal.machine.model if cal.machine else '-',
            'serial_number': cal.machine.serial_number if cal.machine else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.date_calibration,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # กรองข้อมูลตามพารามิเตอร์
    filtered_calibrations = []
    for cal in all_calibrations:
        include_item = True
        
        # กรองตามชื่อเครื่องมือ
        if name_search and name_search.lower() not in cal['machine_name'].lower():
            include_item = False
        
        # กรองตาม Serial Number
        if serial_search and serial_search.lower() not in cal['serial_number'].lower():
            include_item = False
        
        # กรองตามประเภทการสอบเทียบ
        if calibration_type and cal['type'] != calibration_type:
            include_item = False
        
        # กรองตามสถานะ
        if status_filter and cal['status'] != status_filter:
            include_item = False
        
        # กรองตามความเร่งด่วน
        if priority_filter and cal['priority'] != priority_filter:
            include_item = False
        
        if include_item:
            filtered_calibrations.append(cal)
    
    # เรียงลำดับตามระดับความเร่งด่วน: ด่วนมาก -> ด่วน -> ปกติ แล้วตามด้วยวันที่สอบเทียบล่าสุด
    priority_order = {'very_urgent': 1, 'urgent': 2, 'normal': 3}
    filtered_calibrations.sort(key=lambda x: (
        priority_order.get(x['priority'], 4),  # เรียงตามระดับความเร่งด่วน
        x['calibration_date'] if x['calibration_date'] else date.min  # แล้วตามด้วยวันที่
    ))
    
    # ข้อมูลวันที่สำหรับการคำนวณสถานะ
    today = date.today()
    today_plus_30 = today + timedelta(days=30)
    
    context = {
        'force_calibrations_count': CalibrationForce.objects.count(),
        'pressure_calibrations_count': CalibrationPressure.objects.count(),
        'torque_calibrations_count': CalibrationTorque.objects.count(),
        'dial_gauge_calibrations_count': DialGaugeCalibration.objects.count(),
        'balance_calibrations_count': BalanceCalibration.objects.count(),
        'microwave_calibrations_count': MicrowaveCalibration.objects.count(),
        'pending_calibrations_count': (
            CalibrationForce.objects.filter(status='pending').count() +
            CalibrationPressure.objects.filter(status='pending').count() +
            CalibrationTorque.objects.filter(status='pending').count() +
            DialGaugeCalibration.objects.filter(status='pending').count() +
            BalanceCalibration.objects.filter(status='pending').count() +
            MicrowaveCalibration.objects.filter(status='pending').count()
        ),
        'all_calibrations': filtered_calibrations,
        'today': today,
        'today_plus_30': today_plus_30,
    }
    return render(request, 'calibrate/dashboard.html', context)

@login_required
def machine_calibration_list(request, machine_id):
    """แสดงรายการการสอบเทียบของเครื่องมือเฉพาะ"""
    machine = get_object_or_404(Machine, id=machine_id)
    
    # ตรวจสอบประเภทเครื่องมือและดึงข้อมูลการสอบเทียบที่เหมาะสม
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
    """สร้างบันทึกการสอบเทียบสำหรับเครื่องมือเฉพาะ"""
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
        elif 'balance' in machine_type_name:
            form = BalanceCalibrationForm(request.POST)
            template = 'calibrate/balance_form.html'
            success_url = reverse_lazy('machine-calibration-list', kwargs={'machine_id': machine_id})
        else:
            messages.error(request, 'ไม่พบประเภทการสอบเทียบที่เหมาะสม')
            return redirect('machine-list')
        
        if form.is_valid():
            calibration = form.save(commit=False)
            # สำหรับ Balance ใช้ field 'machine' แทน 'uuc_id'
            if 'balance' in machine_type_name:
                calibration.machine = machine
            else:
                calibration.uuc_id = machine.id
            calibration.save()
            messages.success(request, 'บันทึกการสอบเทียบเรียบร้อยแล้ว')
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
        elif 'balance' in machine_type_name:
            form = BalanceCalibrationForm(initial={'machine': machine.id})
            template = 'calibrate/balance_form.html'
        else:
            messages.error(request, 'ไม่พบประเภทการสอบเทียบที่เหมาะสม')
            return redirect('machine-list')
    
    context = {
        'form': form,
        'machine': machine,
        'calibration_type': machine_type_name,
        'machines': Machine.objects.filter(deleted=False).order_by('name'),
    }
    return render(request, template, context)

@login_required
def calibration_by_type(request, calibration_type):
    """แสดงรายการการสอบเทียบตามประเภท"""
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
        messages.error(request, 'ประเภทการสอบเทียบไม่ถูกต้อง')
        return redirect('calibrate-dashboard')
    
    context = {
        'calibrations': calibrations,
        'calibration_type': calibration_type,
    }
    return render(request, template, context)

@login_required
def select_machine_for_calibration(request):
    """หน้าดึงข้อมูลเครื่องมือเพื่อบันทึกการสอบเทียบ"""
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
    """สร้างบันทึกการสอบเทียบพร้อมข้อมูลเครื่องมือ"""
    machine = get_object_or_404(Machine, id=machine_id)
    machine_type_name = machine.machine_type.name.lower()
    
    if request.method == 'POST':
        if 'force' in machine_type_name:
            form = CalibrationForceForm(request.POST)
            template = 'calibrate/force_form_with_machine.html'
            success_url = reverse_lazy('calibrate-dashboard')
        elif 'pressure' in machine_type_name:
            # สำหรับ Pressure ใช้การประมวลผลข้อมูลแบบพิเศษ
            return process_pressure_calibration(request, machine)
        elif 'torque' in machine_type_name:
            # สำหรับ Torque ใช้การประมวลผลข้อมูลแบบพิเศษ
            return process_torque_calibration(request, machine)
        elif 'balance' in machine_type_name:
            form = BalanceCalibrationForm(request.POST)
            template = 'calibrate/balance_form_with_machine.html'
            success_url = reverse_lazy('calibrate-dashboard')
        else:
            messages.error(request, 'ไม่พบประเภทการสอบเทียบที่เหมาะสม')
            return redirect('select-machine-for-calibration')
        
        if form.is_valid():
            calibration = form.save(commit=False)
            # สำหรับ Balance ใช้ field 'machine' แทน 'uuc_id'
            if 'balance' in machine_type_name:
                calibration.machine = machine
            else:
                calibration.uuc_id = machine
            
            # คำนวณวันที่ครบกำหนดถัดไป (+6 เดือน)
            from datetime import datetime, timedelta
            
            if calibration.update:
                # คำนวณ 6 เดือนจากวันที่สอบเทียบ
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
                # ถ้าไม่มีวันที่สอบเทียบ ให้ใช้วันที่ปัจจุบัน + 6 เดือน
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
            messages.success(request, f'บันทึกการสอบเทียบสำหรับ {machine.name} เรียบร้อยแล้ว')
            return redirect(success_url)
    else:
        # เติมข้อมูลเริ่มต้นจากเครื่องมือ
        initial_data = {
            'uuc_id': machine,
        }
        
        if 'force' in machine_type_name:
            form = CalibrationForceForm(initial=initial_data)
            # เพิ่มตัวเลือกผู้ใช้สำหรับฟิลด์ calibrator และ certificate_issuer
            from django.contrib.auth import get_user_model
            User = get_user_model()
            users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
            form.fields['calibrator'].queryset = users
            form.fields['certificate_issuer'].queryset = users
            template = 'calibrate/force_form_with_machine.html'
        elif 'pressure' in machine_type_name:
            form = CalibrationPressureForm(initial=initial_data)
            # เพิ่มตัวเลือกผู้ใช้สำหรับฟิลด์ calibrator และ certificate_issuer
            from django.contrib.auth import get_user_model
            User = get_user_model()
            users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
            form.fields['calibrator'].queryset = users
            form.fields['certificate_issuer'].queryset = users
            template = 'calibrate/pressure_form_with_machine.html'
        elif 'torque' in machine_type_name:
            form = CalibrationTorqueForm(initial=initial_data)
            # เพิ่มตัวเลือกผู้ใช้สำหรับฟิลด์ calibrator และ certificate_issuer
            from django.contrib.auth import get_user_model
            User = get_user_model()
            users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
            form.fields['calibrator'].queryset = users
            form.fields['certificate_issuer'].queryset = users
            template = 'calibrate/torque_form_with_machine.html'
        elif 'balance' in machine_type_name:
            # สำหรับ Balance ใช้ field 'machine' แทน 'uuc_id'
            balance_initial_data = {
                'machine': machine,
            }
            form = BalanceCalibrationForm(initial=balance_initial_data)
            # เพิ่มตัวเลือกผู้ใช้สำหรับฟิลด์ calibrator และ certificate_issuer
            from django.contrib.auth import get_user_model
            User = get_user_model()
            users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
            form.fields['calibrator'].queryset = users
            form.fields['certificate_issuer'].queryset = users
            template = 'calibrate/balance_form_with_machine.html'
        else:
            messages.error(request, 'ไม่พบประเภทการสอบเทียบที่เหมาะสม')
            return redirect('select-machine-for-calibration')
    
    context = {
        'form': form,
        'machine': machine,
        'calibration_type': machine_type_name,
        'machines': Machine.objects.filter(deleted=False).order_by('name'),
    }
    return render(request, template, context)

@login_required
def process_torque_calibration(request, machine):
    """ประมวลผลข้อมูลการสอบเทียบ Torque"""
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
            
            # วันที่สอบเทียบ
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
                    # คำนวณ 6 เดือนจากวันที่สอบเทียบ
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
                # ถ้าไม่มีวันที่สอบเทียบ ให้ใช้วันที่ปัจจุบัน + 6 เดือน
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
            calibrator_id = request.POST.get('calibrator')
            certificate_issuer_id = request.POST.get('certificate_issuer')
            
            calibration.status = status
            calibration.priority = priority
            if std_id and std_id != '':
                calibration.std_id_id = int(std_id)
            if calibrator_id and calibrator_id != '':
                calibration.calibrator_id = int(calibrator_id)
            if certificate_issuer_id and certificate_issuer_id != '':
                calibration.certificate_issuer_id = int(certificate_issuer_id)
            
            print("=== DEBUG: บันทึกข้อมูล ===")
            calibration.save()
            print(f"บันทึกสำเร็จ! ID: {calibration.cal_torque_id}")
            
            messages.success(request, f'บันทึกการสอบเทียบ Torque สำหรับ {machine.name} เรียบร้อยแล้ว')
            return redirect('calibrate-dashboard')
            
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
    """ประมวลผลข้อมูลการสอบเทียบ Pressure"""
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
                    # คำนวณ 6 เดือนจากวันที่สอบเทียบ
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
                # ถ้าไม่มีวันที่สอบเทียบ ให้ใช้วันที่ปัจจุบัน + 6 เดือน
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
            calibrator_id = request.POST.get('calibrator')
            certificate_issuer_id = request.POST.get('certificate_issuer')
            
            calibration.status = status
            calibration.priority = priority
            if std_id and std_id != '':
                calibration.std_id_id = int(std_id)
            if calibrator_id and calibrator_id != '':
                calibration.calibrator_id = int(calibrator_id)
            if certificate_issuer_id and certificate_issuer_id != '':
                calibration.certificate_issuer_id = int(certificate_issuer_id)
            
            print("=== DEBUG: บันทึกข้อมูล ===")
            calibration.save()
            print(f"บันทึกสำเร็จ! ID: {calibration.cal_pressure_id}")
            
            messages.success(request, f'บันทึกการสอบเทียบ Pressure สำหรับ {machine.name} เรียบร้อยแล้ว')
            return redirect('calibrate-dashboard')
            
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
    """หน้ารายงานสอบเทียบ"""
    from datetime import date, timedelta
    
    # ดึงข้อมูลการสอบเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    balance_calibrations = BalanceCalibration.objects.select_related('machine', 'std_id', 'calibrator', 'certificate_issuer').all()
    
    # รวมข้อมูลการสอบเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การสอบเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การสอบเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การสอบเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Balance calibrations
    for cal in balance_calibrations:
        all_calibrations.append({
            'id': cal.id,
            'type': 'balance',
            'type_name': 'การสอบเทียบ Balance',
            'machine_name': cal.machine.name if cal.machine else '-',
            'machine_model': cal.machine.model if cal.machine else '-',
            'serial_number': cal.machine.serial_number if cal.machine else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.date_calibration,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.date_calibration,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เรียงลำดับตามวันที่สอบเทียบล่าสุด
    all_calibrations.sort(key=lambda x: x['calibration_date'] if x['calibration_date'] else date.min, reverse=True)
    
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
    """หน้ารายงานผลสอบเทียบแบบละเอียด"""
    from datetime import date, timedelta
    
    # รับพารามิเตอร์การกรอง
    department = request.GET.get('department', '')
    instrument_type = request.GET.get('instrument_type', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    serial_search = request.GET.get('serial_search', '')
    name_search = request.GET.get('name_search', '')
    status_filter = request.GET.get('status_filter', '')
    
    # ดึงข้อมูลหน่วยงาน (Organize) สำหรับที่อยู่
    from organize.models import Organize
    try:
        # หาหน่วยงานหลัก (main unit) หรือหน่วยงานแรก
        organization = Organize.objects.filter(is_main_unit=True).first()
        if not organization:
            organization = Organize.objects.first()
    except:
        organization = None
    
    # ดึงข้อมูลการสอบเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    balance_calibrations = BalanceCalibration.objects.select_related('machine', 'std_id', 'calibrator', 'certificate_issuer').all()
    
    # รวมข้อมูลการสอบเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การสอบเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การสอบเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การสอบเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Balance calibrations
    for cal in balance_calibrations:
        all_calibrations.append({
            'id': cal.id,
            'type': 'balance',
            'type_name': 'การสอบเทียบ Balance',
            'machine_name': cal.machine.name if cal.machine else '-',
            'machine_model': cal.machine.model if cal.machine else '-',
            'serial_number': cal.machine.serial_number if cal.machine else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.date_calibration,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.date_calibration,  # วันที่สอบเทียบ
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
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
            elif instrument_type == 'balance' and cal['type'] != 'balance':
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
    
    # เรียงลำดับตามวันที่สอบเทียบล่าสุด
    filtered_calibrations.sort(key=lambda x: x['calibration_date'] if x['calibration_date'] else date.min, reverse=True)
    
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
            CalibrationTorque.objects.count() +
            BalanceCalibration.objects.count()
        ),
        'all_calibrations': filtered_calibrations,
        'today': today,
        'today_plus_30': today_plus_30,
        'organization': organization,  # เพิ่มข้อมูลหน่วยงาน
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
    """Export รายงานสอบเทียบเป็นไฟล์ Word"""
    from datetime import date, timedelta
    
    # รับพารามิเตอร์การกรอง (เหมือนกับใน calibration_report_detail)
    department = request.GET.get('department', '')
    instrument_type = request.GET.get('instrument_type', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    serial_search = request.GET.get('serial_search', '')
    name_search = request.GET.get('name_search', '')
    status_filter = request.GET.get('status_filter', '')
    
    # ดึงข้อมูลหน่วยงาน (Organize) สำหรับที่อยู่
    from organize.models import Organize
    try:
        # หาหน่วยงานหลัก (main unit) หรือหน่วยงานแรก
        organization = Organize.objects.filter(is_main_unit=True).first()
        if not organization:
            organization = Organize.objects.first()
    except:
        organization = None
    
    # ดึงข้อมูลการสอบเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    
    # รวมข้อมูลการสอบเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การสอบเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การสอบเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การสอบเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
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
            elif instrument_type == 'balance' and cal['type'] != 'balance':
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
    
    # เรียงลำดับตามวันที่สอบเทียบล่าสุด
    filtered_calibrations.sort(key=lambda x: x['calibration_date'] if x['calibration_date'] else date.min, reverse=True)
    
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
    title = doc.add_heading('รายงานสอบเทียบ', 0)
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
        user_unit = organization.name if organization else 'ยังไม่ได้กรอก'
        row_cells[4].text = user_unit
        row_cells[4].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # จำนวน
        row_cells[5].text = '๑'
        row_cells[5].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # หมายเหตุ
        if cal['status'] in ['cert_issued', 'passed', 'active']:
            remark = 'ออกใบรับรอง'
        elif cal['status'] in ['failed', 'pending', 'in_progress', 'not_set']:
            remark = 'ไม่ผ่านการสอบเทียบ'
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
    response['Content-Disposition'] = f'attachment; filename="รายงานสอบเทียบ_{datetime.now().strftime("%Y%m%d")}.docx"'
    
    return response

@login_required
def export_to_excel(request):
    """Export รายงานสอบเทียบเป็นไฟล์ Excel"""
    from datetime import date, timedelta
    
    # รับพารามิเตอร์การกรอง (เหมือนกับใน calibration_report_detail)
    department = request.GET.get('department', '')
    instrument_type = request.GET.get('instrument_type', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    serial_search = request.GET.get('serial_search', '')
    name_search = request.GET.get('name_search', '')
    status_filter = request.GET.get('status_filter', '')
    
    # ดึงข้อมูลหน่วยงาน (Organize) สำหรับที่อยู่
    from organize.models import Organize
    try:
        # หาหน่วยงานหลัก (main unit) หรือหน่วยงานแรก
        organization = Organize.objects.filter(is_main_unit=True).first()
        if not organization:
            organization = Organize.objects.first()
    except:
        organization = None
    
    # ดึงข้อมูลการสอบเทียบทั้งหมด
    force_calibrations = CalibrationForce.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    pressure_calibrations = CalibrationPressure.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    torque_calibrations = CalibrationTorque.objects.select_related('uuc_id', 'std_id', 'calibrator', 'certificate_issuer').all()
    
    # รวมข้อมูลการสอบเทียบทั้งหมด
    all_calibrations = []
    
    # เพิ่มข้อมูล Force calibrations
    for cal in force_calibrations:
        all_calibrations.append({
            'id': cal.cal_force_id,
            'type': 'force',
            'type_name': 'การสอบเทียบแรง',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Pressure calibrations
    for cal in pressure_calibrations:
        all_calibrations.append({
            'id': cal.cal_pressure_id,
            'type': 'pressure',
            'type_name': 'การสอบเทียบความดัน',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
        })
    
    # เพิ่มข้อมูล Torque calibrations
    for cal in torque_calibrations:
        all_calibrations.append({
            'id': cal.cal_torque_id,
            'type': 'torque',
            'type_name': 'การสอบเทียบแรงบิด',
            'machine_name': cal.uuc_id.name if cal.uuc_id else '-',
            'machine_model': cal.uuc_id.model if cal.uuc_id else '-',
            'serial_number': cal.uuc_id.serial_number if cal.uuc_id else '-',
            'std_name': cal.std_id.name if cal.std_id else '-',
            'update_date': cal.update,
            'next_due': cal.next_due,
            'status': cal.status,
            'priority': cal.priority,
            'calibration_date': cal.update,  # ǹ��ͺ�º
            'calibrator': cal.calibrator.get_full_name() if cal.calibrator else '-',
            'certificate_issuer': cal.certificate_issuer.get_full_name() if cal.certificate_issuer else '-',
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
            elif instrument_type == 'balance' and cal['type'] != 'balance':
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
    
    # เรียงลำดับตามวันที่สอบเทียบล่าสุด
    filtered_calibrations.sort(key=lambda x: x['calibration_date'] if x['calibration_date'] else date.min, reverse=True)
    
    # สร้าง Excel workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "รายงานสอบเทียบ"
    
    # ตั้งค่าหัวเรื่อง
    title_font = Font(name='TH Sarabun New', size=16, bold=True)
    header_font = Font(name='TH Sarabun New', size=12, bold=True)
    cell_font = Font(name='TH Sarabun New', size=11)
    
    # สีสำหรับ header
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    
    # หัวเรื่อง
    ws['A1'] = 'รายงานสอบเทียบ'
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
        user_unit = organization.name if organization else 'ยังไม่ได้กรอก'
        ws.cell(row=row, column=5, value=user_unit).alignment = Alignment(horizontal='center')
        
        # จำนวน
        ws.cell(row=row, column=6, value='๑').alignment = Alignment(horizontal='center')
        
        # หมายเหตุ
        if cal['status'] in ['cert_issued', 'passed', 'active']:
            remark = 'ออกใบรับรอง'
        elif cal['status'] in ['failed', 'pending', 'in_progress', 'not_set']:
            remark = 'ไม่ผ่านการสอบเทียบ'
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
    response['Content-Disposition'] = f'attachment; filename="รายงานสอบเทียบ_{datetime.now().strftime("%Y%m%d")}.xlsx"'
    
    return response

@login_required
def increase_priority(request, cal_type, cal_id):
    """เพิ่มระดับความเร่งด่วนของการสอบเทียบ"""
    # ตรวจสอบสิทธิ์ - เฉพาะเจ้าหน้าที่และ admin
    if not (request.user.is_staff or request.user.is_superuser):
        return JsonResponse({
            'success': False,
            'message': 'คุณไม่มีสิทธิ์ในการเพิ่มระดับความเร่งด่วน'
        })
    
    try:
        # รับข้อมูลจาก request
        import json
        data = json.loads(request.body)
        new_priority = data.get('new_priority')
        
        if not new_priority:
            return JsonResponse({
                'success': False,
                'message': 'ไม่พบข้อมูลระดับความเร่งด่วนใหม่'
            })
        
        # ตรวจสอบระดับความเร่งด่วนที่ถูกต้อง
        valid_priorities = ['normal', 'urgent', 'very_urgent']
        if new_priority not in valid_priorities:
            return JsonResponse({
                'success': False,
                'message': 'ระดับความเร่งด่วนไม่ถูกต้อง'
            })
        
        # ดึงข้อมูลการสอบเทียบตามประเภท
        if cal_type == 'force':
            calibration = get_object_or_404(CalibrationForce, cal_force_id=cal_id)
        elif cal_type == 'pressure':
            calibration = get_object_or_404(CalibrationPressure, cal_pressure_id=cal_id)
        elif cal_type == 'torque':
            calibration = get_object_or_404(CalibrationTorque, cal_torque_id=cal_id)
        elif cal_type == 'balance':
            calibration = get_object_or_404(BalanceCalibration, pk=cal_id)
        else:
            return JsonResponse({
                'success': False,
                'message': 'ประเภทการสอบเทียบไม่ถูกต้อง'
            })
        
        # ตรวจสอบว่าการเปลี่ยนระดับมีความหมายหรือไม่
        current_priority = calibration.priority
        if current_priority == new_priority:
            return JsonResponse({
                'success': False,
                'message': 'ระดับความเร่งด่วนนี้เป็นระดับปัจจุบันอยู่แล้ว'
            })
        
        # อัปเดตระดับความเร่งด่วน
        calibration.priority = new_priority
        calibration.save()
        
        # สร้างข้อความตอบกลับ
        priority_names = {
            'normal': 'ปกติ',
            'urgent': 'ด่วน',
            'very_urgent': 'ด่วนมาก'
        }
        
        return JsonResponse({
            'success': True,
            'message': f'เปลี่ยนระดับความเร่งด่วนเป็น "{priority_names[new_priority]}" สำเร็จ',
            'old_priority': current_priority,
            'new_priority': new_priority
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'เกิดข้อผิดพลาด: {str(e)}'
        })

@login_required
def close_work(request, cal_type, cal_id):
    """ปิดงานการสอบเทียบ"""
    # ตรวจสอบสิทธิ์ - เฉพาะเจ้าหน้าที่และ admin
    if not (request.user.is_staff or request.user.is_superuser):
        return JsonResponse({
            'success': False,
            'message': 'คุณไม่มีสิทธิ์ในการปิดงาน'
        })
    
    try:
        # ดึงข้อมูลการสอบเทียบตามประเภท
        if cal_type == 'force':
            calibration = get_object_or_404(CalibrationForce, cal_force_id=cal_id)
        elif cal_type == 'pressure':
            calibration = get_object_or_404(CalibrationPressure, cal_pressure_id=cal_id)
        elif cal_type == 'torque':
            calibration = get_object_or_404(CalibrationTorque, cal_torque_id=cal_id)
        elif cal_type == 'balance':
            calibration = get_object_or_404(BalanceCalibration, pk=cal_id)
        else:
            return JsonResponse({
                'success': False,
                'message': 'ประเภทการสอบเทียบไม่ถูกต้อง'
            })
        
        # ตรวจสอบสถานะปัจจุบัน
        current_status = calibration.status
        if current_status == 'closed':
            return JsonResponse({
                'success': False,
                'message': 'งานนี้ถูกปิดแล้ว'
            })
        
        # อัปเดตสถานะเป็นปิดงาน
        calibration.status = 'closed'
        calibration.save()
        
        return JsonResponse({
            'success': True,
            'message': 'ปิดงานสำเร็จ',
            'old_status': current_status,
            'new_status': 'closed'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'เกิดข้อผิดพลาด: {str(e)}'
        })

@login_required
def export_certificate_excel(request, cal_id, cal_type):
    """Export ใบรับรองแบบ Excel (แบบจำลอง)"""
    try:
        # ดึงข้อมูลการสอบเทียบตามประเภท
        if cal_type == 'force':
            calibration = get_object_or_404(CalibrationForce, cal_force_id=cal_id)
        elif cal_type == 'pressure':
            calibration = get_object_or_404(CalibrationPressure, cal_pressure_id=cal_id)
        elif cal_type == 'torque':
            calibration = get_object_or_404(CalibrationTorque, cal_torque_id=cal_id)
        elif cal_type == 'balance':
            calibration = get_object_or_404(BalanceCalibration, pk=cal_id)
        else:
            messages.error(request, 'ประเภทการสอบเทียบไม่ถูกต้อง')
            return redirect('calibrate-report-detail')
        
        # ตรวจสอบสถานะว่าผ่านการสอบเทียบหรือไม่
        if calibration.status not in ['cert_issued', 'passed', 'active']:
            messages.error(request, 'ไม่สามารถออกใบรับรองได้ เนื่องจากยังไม่ผ่านการสอบเทียบ')
            return redirect('calibrate-report-detail')
        
        # สร้างไฟล์ Excel แบบจำลอง
        wb = Workbook()
        ws = wb.active
        ws.title = "ใบรับรองการสอบเทียบ"
        
        # กำหนดขนาดคอลัมน์
        ws.column_dimensions['A'].width = 20
        ws.column_dimensions['B'].width = 30
        ws.column_dimensions['C'].width = 20
        ws.column_dimensions['D'].width = 30
        
        # หัวข้อหลัก
        ws.merge_cells('A1:D1')
        ws['A1'] = 'ใบรับรองการสอบเทียบเครื่องมือวัด'
        ws['A1'].font = Font(name='TH Sarabun New', size=18, bold=True)
        ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
        
        # ข้อมูลเครื่องมือ
        row = 3
        ws[f'A{row}'] = 'ชื่อเครื่องมือ:'
        ws[f'B{row}'] = calibration.uuc_id.name if calibration.uuc_id else '-'
        ws[f'C{row}'] = 'รุ่น:'
        ws[f'D{row}'] = calibration.uuc_id.model if calibration.uuc_id and calibration.uuc_id.model else '-'
        
        row += 1
        ws[f'A{row}'] = 'Serial Number:'
        ws[f'B{row}'] = calibration.uuc_id.serial_number if calibration.uuc_id and calibration.uuc_id.serial_number else '-'
        ws[f'C{row}'] = 'ผู้ผลิต:'
        ws[f'D{row}'] = str(calibration.uuc_id.manufacture) if calibration.uuc_id and calibration.uuc_id.manufacture else '-'
        
        row += 1
        ws[f'A{row}'] = 'วันที่สอบเทียบ:'
        ws[f'B{row}'] = calibration.update.strftime('%d/%m/%Y') if calibration.update else '-'
        ws[f'C{row}'] = 'วันที่ครบกำหนด:'
        ws[f'D{row}'] = calibration.next_due.strftime('%d/%m/%Y') if calibration.next_due else '-'
        
        row += 1
        ws[f'A{row}'] = 'ผลการสอบเทียบ:'
        ws[f'B{row}'] = 'ผ่านการสอบเทียบ'
        ws[f'B{row}'].font = Font(color='008000', bold=True)  # สีเขียว
        
        row += 2
        ws[f'A{row}'] = 'หมายเหตุ:'
        ws[f'B{row}'] = 'นี่เป็นแบบจำลองใบรับรอง - รอไฟล์ template จริง'
        ws[f'B{row}'].font = Font(italic=True, color='FF0000')  # สีแดง ตัวเอียง
        
        # กำหนดรูปแบบตัวอักษร
        for row in range(3, 8):
            for col in ['A', 'B', 'C', 'D']:
                cell = ws[f'{col}{row}']
                cell.font = Font(name='TH Sarabun New', size=12)
                cell.alignment = Alignment(vertical='center')
        
        # สร้าง response
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        
        # สร้างชื่อไฟล์ที่ปลอดภัย
        machine_name = calibration.uuc_id.name if calibration.uuc_id else "เครื่องมือ"
        safe_filename = f"ใบรับรอง_{machine_name}_{datetime.now().strftime('%Y%m%d')}.xlsx"
        
        response['Content-Disposition'] = f'attachment; filename="{safe_filename}"'
        
        wb.save(response)
        return response
        
    except Exception as e:
        messages.error(request, f'เกิดข้อผิดพลาดในการสร้างใบรับรอง: {str(e)}')
        return redirect('calibrate-report-detail')

@login_required
def export_balance_certificate_docx(request, cal_id):
    """Export ใบรับรอง Balance แบบ DOCX โดยใช้ template"""
    try:
        # ดึงข้อมูลการสอบเทียบ Balance
        calibration = get_object_or_404(BalanceCalibration, pk=cal_id)
        
        # ตรวจสอบสถานะว่าผ่านการสอบเทียบหรือไม่
        if calibration.status not in ['cert_issued', 'passed', 'active']:
            messages.error(request, 'ไม่สามารถออกใบรับรองได้ เนื่องจากยังไม่ผ่านการสอบเทียบ')
            return redirect('calibrate-report-detail')
        
        # เปิด template
        template_path = 'Balance_template.docx'
        doc = Document(template_path)
        
        # ข้อมูลเครื่องมือ
        machine = calibration.machine
        standard = calibration.std_id
        
        # ดึงข้อมูลหน่วยงาน (Organize) สำหรับที่อยู่
        from organize.models import Organize
        try:
            # หาหน่วยงานหลัก (main unit) หรือหน่วยงานแรก
            organization = Organize.objects.filter(is_main_unit=True).first()
            if not organization:
                organization = Organize.objects.first()
        except:
            organization = None
        
        # สร้าง dictionary สำหรับแทนค่า
        replacements = {
            # ข้อมูลเครื่องมือ
            '{{MODEL}}': machine.model if machine.model else '-',
            '{{MANUFACTURER}}': str(machine.manufacture) if machine.manufacture else '-',
            '{{DESCRIPTION}}': machine.name if machine.name else '-',
            '{{SERIAL_NUMBER}}': machine.serial_number if machine.serial_number else '-',
            '{{RANGE}}': machine.range if machine.range else '-',
            '{{GRADUATION}}': machine.res_uuc if machine.res_uuc else '-',
            '{{OPTION}}': machine.option if machine.option else 'N/A',
            '{{CUSTOMER_ASSET_ID}}': machine.customer_asset_id if machine.customer_asset_id else '-',
            
            # ข้อมูลการสอบเทียบ
            '{{RECEIVED_DATE}}': calibration.received_date.strftime('%d-%b-%Y') if calibration.received_date else '-',
            '{{DATE_OF_CALIBRATION}}': calibration.date_calibration.strftime('%d-%b-%Y') if calibration.date_calibration else '-',
            '{{DUE_DATE}}': calibration.next_due.strftime('%d-%b-%Y') if calibration.next_due else '-',
            '{{ISSUE_DATE}}': calibration.issue_date.strftime('%d-%b-%Y') if calibration.issue_date else '-',
            '{{CERTIFICATE_NUMBER}}': calibration.certificate_number if calibration.certificate_number else '-',
            '{{PROCEDURE}}': calibration.procedure_number if calibration.procedure_number else '-',
            
            # ข้อมูลมาตรฐาน
            '{{STANDARD_ASSET_NO}}': standard.asset_number if standard and standard.asset_number else '-',
            '{{STANDARD_DESCRIPTION}}': standard.name if standard else '-',
            '{{STANDARD_MAKER_MODEL}}': standard.description if standard and standard.description else '-',
            '{{STANDARD_SERIAL}}': standard.name if standard else '-',  # ใช้ name เป็น serial ถ้าไม่มี field แยก
            '{{STANDARD_CERTIFICATE}}': standard.certificate_number if standard and standard.certificate_number else '-',
            '{{STANDARD_DUE_DATE}}': standard.due_date.strftime('%d-%b-%Y') if standard and standard.due_date else '-',
            
            # ข้อมูลผู้รับผิดชอบ
            '{{CALIBRATOR}}': str(calibration.calibrator) if calibration.calibrator else '-',
            '{{APPROVER}}': str(calibration.certificate_issuer) if calibration.certificate_issuer else '-',
            
            # ข้อมูลหน่วยงานและที่อยู่
            '{{CUSTOMER}}': organization.name if organization else 'Physical Lab, Metrology Division, DC&E (Royal Thai Air Force)',
            '{{CUSTOMER_ADDRESS}}': organization.address if organization and organization.address else '171 Building. No2025 Sanambin, Donmueang\nBangkok, 10210',
            '{{LOCATION_OF_CALIBRATION}}': organization.name if organization else 'Metrology Division, DC&E (Royal Thai Air Force)',
            '{{LOCATION_ADDRESS}}': organization.address if organization and organization.address else '171 Building. No2025 Sanambin, Donmueang\nBangkok, 10210',
        }
        
        # ฟังก์ชันสำหรับแทนค่าใน paragraph
        def replace_in_paragraph(paragraph, replacements):
            for placeholder, value in replacements.items():
                if placeholder in paragraph.text:
                    # แทนที่ข้อความใน paragraph
                    for run in paragraph.runs:
                        if placeholder in run.text:
                            run.text = run.text.replace(placeholder, value)
        
        # ฟังก์ชันสำหรับแทนค่าใน text box และ shape
        def replace_in_shapes(shapes, replacements):
            for shape in shapes:
                if hasattr(shape, 'text_frame'):
                    for paragraph in shape.text_frame.paragraphs:
                        replace_in_paragraph(paragraph, replacements)
                if hasattr(shape, 'shapes'):
                    replace_in_shapes(shape.shapes, replacements)
        
        # ฟังก์ชันสำหรับแทนค่าใน document ทั้งหมด
        def replace_in_document(doc, replacements):
            # แทนค่าใน paragraphs
            for paragraph in doc.paragraphs:
                replace_in_paragraph(paragraph, replacements)
            
            # แทนค่าใน tables
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        for paragraph in cell.paragraphs:
                            replace_in_paragraph(paragraph, replacements)
            
            # แทนค่าใน headers และ footers
            for section in doc.sections:
                # Header
                if section.header:
                    for paragraph in section.header.paragraphs:
                        replace_in_paragraph(paragraph, replacements)
                
                # Footer
                if section.footer:
                    for paragraph in section.footer.paragraphs:
                        replace_in_paragraph(paragraph, replacements)
                
                # Text boxes และ shapes
                if hasattr(section, 'shapes'):
                    replace_in_shapes(section.shapes, replacements)
        
        # เรียกใช้ฟังก์ชันแทนค่าใน document ทั้งหมด
        replace_in_document(doc, replacements)
        
        # เพิ่มข้อมูลผลการสอบเทียบในตาราง (ถ้ามี)
        readings = calibration.readings.all().order_by('uuc_set')
        if readings:
            # หาตารางผลการสอบเทียบใน template (ตารางที่ 7 - Calibration Results)
            table_count = 0
            for table in doc.tables:
                table_count += 1
                # ตรวจสอบว่าตารางนี้เป็นตารางผลการสอบเทียบหรือไม่ (ตารางที่ 7)
                if table_count == 7 and len(table.rows) > 1 and len(table.columns) >= 5:
                    second_row_text = ' '.join([cell.text.strip() for cell in table.rows[1].cells])
                    if 'Nominal Value' in second_row_text or 'Conventional Mass' in second_row_text:
                        # ลบแถวเก่า (ยกเว้น header 2 แถวแรก)
                        for i in range(len(table.rows) - 1, 1, -1):
                            table._tbl.remove(table.rows[i]._tr)
                        
                        # เพิ่มข้อมูลการอ่านค่าใหม่
                        for reading in readings:
                            row_cells = table.add_row().cells
                            
                            # คำนวณ Error = Displayed Value - Conventional Mass
                            error_value = None
                            if reading.displayed_value and reading.conventional_mass:
                                error_value = float(reading.displayed_value) - float(reading.conventional_mass)
                            
                            # เติมข้อมูลในแต่ละคอลัมน์
                            if len(row_cells) >= 1:
                                row_cells[0].text = str(reading.uuc_set) if reading.uuc_set else '-'
                            if len(row_cells) >= 2:
                                row_cells[1].text = str(reading.conventional_mass) if reading.conventional_mass else '-'
                            if len(row_cells) >= 3:
                                row_cells[2].text = str(reading.displayed_value) if reading.displayed_value else '-'
                            if len(row_cells) >= 4:
                                row_cells[3].text = f"{error_value:.5f}" if error_value is not None else '-'
                            if len(row_cells) >= 5:
                                row_cells[4].text = str(reading.uncertainty) if reading.uncertainty else '-'
                            
                            # จัดรูปแบบแถวข้อมูล
                            for cell in row_cells:
                                for paragraph in cell.paragraphs:
                                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                                    for run in paragraph.runs:
                                        run.font.name = 'TH Sarabun New'
                                        run.font.size = Pt(10)
                        break
        
        # สร้าง response
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        
        # สร้างชื่อไฟล์ที่ปลอดภัย
        machine_name = machine.name if machine else "Balance"
        safe_filename = f"Balance_Certificate_{machine_name}_{datetime.now().strftime('%Y%m%d')}.docx"
        
        response['Content-Disposition'] = f'attachment; filename="{safe_filename}"'
        
        # บันทึกเอกสาร
        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0)
        response.write(buffer.getvalue())
        
        return response
        
    except Exception as e:
        messages.error(request, f'เกิดข้อผิดพลาดในการสร้างใบรับรอง: {str(e)}')
        return redirect('calibrate-report-detail')

from docxtpl import DocxTemplate
def export_certificate(request, pk):
    calibration = CalibrationForce.objects.get(pk=pk)

    doc = DocxTemplate("Balance_template.docx")

    context = {
        "MODEL": calibration.uuc_id.name if calibration.uuc_id else "",
        "MANUFACTURER": calibration.uuc_id.manufacturer if hasattr(calibration.uuc_id, "manufacturer") else "",
        "DESCRIPTION": calibration.uuc_id.name if calibration.uuc_id else "",
        "SERIAL_NUMBER": getattr(calibration.uuc_id, "serial_number", ""),
        "RANGE": getattr(calibration.uuc_id, "range", ""),
        "GRADUATION": getattr(calibration.uuc_id, "graduation", ""),
        "OPTION": getattr(calibration.uuc_id, "option", ""),
        "CERTIFICATE_NUMBER": getattr(calibration, "certificate_number", ""),
        "CUSTOMER_ASSET_ID": getattr(calibration, "customer_asset_id", ""),
        "PROCEDURE": getattr(calibration, "procedure", ""),
        "RECEIVED_DATE": calibration.update,
        "DATE_OF_CALIBRATION": calibration.update,
        "DUE_DATE": calibration.next_due,
        "ISSUE_DATE": calibration.update,
        "CALIBRATOR": calibration.calibrator.get_full_name() if calibration.calibrator else "",
        "APPROVER": calibration.certificate_issuer.get_full_name() if calibration.certificate_issuer else "",
        "CUSTOMER_ADDRESS": getattr(calibration.uuc_id, "address", ""),
        "LOCATION_OF_CALIBRATION": "กบร.ทร.",
        "LOCATION_ADDRESS": "Somewhere Navy Base",
    }

    doc.render(context)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    response["Content-Disposition"] = f'attachment; filename="certificate_{calibration.pk}.docx"'
    doc.save(response)
    return response