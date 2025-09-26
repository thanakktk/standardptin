from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import datetime, timedelta

# Import models
from machine.models import Machine
from calibrate.models import CalibrationPressure, CalibrationTorque
from cert.models import Certificate
from employee.models import Employee
from organize.models import Organize

@login_required
def home(request):
    # ดึงข้อมูลสถิติจาก database
    context = {
        'machine_count': Machine.objects.count(),
        'calibration_count': (
            CalibrationPressure.objects.count() + 
            CalibrationTorque.objects.count()
        ),
        'cert_count': Certificate.objects.count(),
        'employee_count': Employee.objects.count(),
        'organize_count': Organize.objects.count(),
        
        # ข้อมูลเพิ่มเติมสำหรับ dashboard
        'recent_machines': Machine.objects.order_by('-update')[:5],
        'recent_calibrations': CalibrationPressure.objects.order_by('-cal_pressure_id')[:5],
        'recent_certificates': Certificate.objects.order_by('-created_at')[:5],
        
        # สถิติตามประเภท
        'machine_types': Machine.objects.values('machine_type__name').annotate(count=Count('id')).order_by('-count')[:5],
        'organizations': Organize.objects.annotate(machine_count=Count('machine')).order_by('-machine_count')[:5],
        
        # ข้อมูลใบรับรองที่ใกล้หมดอายุ
        'expiring_certs': Certificate.objects.filter(
            expire_date__gte=datetime.now().date(),
            expire_date__lte=datetime.now().date() + timedelta(days=30)
        ).count(),
        
        # ข้อมูลใบรับรองที่หมดอายุแล้ว
        'expired_certs': Certificate.objects.filter(
            expire_date__lt=datetime.now().date()
        ).count(),
        
        # ข้อมูลใบรับรองที่ยังไม่หมดอายุ
        'valid_certs': Certificate.objects.filter(
            expire_date__gte=datetime.now().date()
        ).count(),
        
        # วันที่ปัจจุบัน
        'today': datetime.now().date(),
    }
    
    return render(request, 'home.html', context) 