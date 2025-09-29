#!/usr/bin/env python
"""
Test script เพื่อทดสอบการแก้ไขปัญหาเครื่องมือซ้ำ
"""
import os
import sys
import django

# เพิ่ม path ของ project
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ตั้งค่า Django ก่อน import อื่นๆ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projest.settings')
django.setup()

from django.test import Client
from accounts.models import User
from calibrate.models import CalibrationPressure, CalibrationEquipmentUsed
from machine.models import CalibrationEquipment

def test_pressure_fixed():
    print("=== ทดสอบการแก้ไขปัญหาเครื่องมือซ้ำ ===")
    
    # สร้าง test client
    client = Client()
    
    # หา user และให้สิทธิ์
    user = User.objects.first()
    user.is_staff = True
    user.is_superuser = True
    user.save()
    client.force_login(user)
    
    # หา Pressure record
    pressure = CalibrationPressure.objects.first()
    print(f"✅ ใช้ Pressure ID: {pressure.cal_pressure_id}")
    
    # ดูเครื่องมือที่มี
    equipments = CalibrationEquipment.objects.all()
    print(f"✅ เครื่องมือที่มี: {[f'{eq.id}-{eq.name}' for eq in equipments]}")
    
    if len(equipments) < 2:
        print("❌ ต้องมีเครื่องมืออย่างน้อย 2 ตัว")
        return
    
    # ใช้เครื่องมือที่มี (2 ตัว)
    equipment_ids = [eq.id for eq in equipments[:2]]
    selected_equipment = ','.join(map(str, equipment_ids))
    
    # จำลองการส่งข้อมูลแบบเดียวกับฟอร์ม
    form_data = {
        'measurement_range': '0-100',
        'set': '50',
        'm1': '49.8',
        'm2': '50.1',
        'm3': '49.9',
        'm4': '50.0',
        'avg': 49.95,
        'actual': 50.0,
        'error': 0.05,
        'status': 'passed',
        'priority': 'normal',
        'uuc_id': pressure.uuc_id.id,
        'std_id': equipments[0].id,  # เครื่องมือหลัก
        'calibrator': user.id,
        'certificate_issuer': user.id,
        'certificate_number': 'TEST-002',
        'selected_equipment': selected_equipment,  # เครื่องมือที่มี
    }
    
    print(f"✅ ข้อมูลที่จะส่ง: selected_equipment = '{form_data['selected_equipment']}'")
    
    # ส่งข้อมูลไปยัง form
    url = f'/calibrate/pressure/{pressure.cal_pressure_id}/edit/'
    response = client.post(url, data=form_data)
    
    print(f"✅ Response status: {response.status_code}")
    
    if response.status_code == 302:
        print("✅ บันทึกสำเร็จ! (Redirect)")
        
        # ตรวจสอบข้อมูลที่บันทึก
        print("\n=== ตรวจสอบข้อมูลหลังบันทึก ===")
        
        equipment_used = CalibrationEquipmentUsed.objects.filter(
            calibration_type='pressure',
            calibration_id=pressure.cal_pressure_id
        )
        print(f"✅ เครื่องมือที่ใช้สอบเทียบ: {equipment_used.count()} ตัว")
        
        for eq in equipment_used:
            print(f"  - {eq.equipment.name} (ID: {eq.equipment.id})")
        
        # ตรวจสอบไม่ซ้ำ
        equipment_ids = [eq.equipment.id for eq in equipment_used]
        unique_ids = list(set(equipment_ids))
        print(f"✅ เครื่องมือไม่ซ้ำ: {len(unique_ids) == len(equipment_ids)}")
        
    else:
        print(f"❌ Error: {response.status_code}")

if __name__ == "__main__":
    test_pressure_fixed()
