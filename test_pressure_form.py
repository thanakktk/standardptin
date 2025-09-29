#!/usr/bin/env python
"""
Test script เพื่อทดสอบการเพิ่มเครื่องมือ 2 ตัวผ่านฟอร์ม Pressure
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

def test_pressure_form_with_equipment():
    print("=== ทดสอบการเพิ่มเครื่องมือ 2 ตัวผ่านฟอร์ม Pressure ===")
    
    # สร้าง test client
    client = Client()
    
    # หา user สำหรับ login
    try:
        user = User.objects.first()
        if not user:
            print("❌ ไม่พบ User ในระบบ")
            return
        print(f"✅ ใช้ User: {user.username}")
        
        # ให้สิทธิ์ user
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f"✅ ให้สิทธิ์ admin: {user.is_superuser}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # Login
    login_success = client.force_login(user)
    print(f"✅ Login: {login_success}")
    
    # หา Pressure record ที่มีอยู่
    pressure = CalibrationPressure.objects.first()
    if not pressure:
        print("❌ ไม่พบ Pressure record")
        return
    
    print(f"✅ ใช้ Pressure ID: {pressure.cal_pressure_id}")
    
    # ดูเครื่องมือที่มีในระบบ
    equipments = CalibrationEquipment.objects.all()[:3]
    print(f"✅ เครื่องมือที่มี: {[f'{eq.id}-{eq.name}' for eq in equipments]}")
    
    if len(equipments) < 2:
        print("❌ ต้องมีเครื่องมืออย่างน้อย 2 ตัว")
        return
    
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
        'certificate_number': 'TEST-001',
        'selected_equipment': f'{equipments[0].id},{equipments[1].id}',  # เครื่องมือ 2 ตัว
        'std_id_1': equipments[1].id,  # เครื่องมือเพิ่มเติม
    }
    
    print(f"✅ ข้อมูลที่จะส่ง: {form_data}")
    
    # ส่งข้อมูลไปยัง form
    url = f'/calibrate/pressure/{pressure.cal_pressure_id}/edit/'
    print(f"✅ URL: {url}")
    
    try:
        response = client.post(url, data=form_data)
        print(f"✅ Response status: {response.status_code}")
        
        if response.status_code == 302:  # Redirect after successful save
            print("✅ บันทึกสำเร็จ! (Redirect)")
        else:
            print(f"⚠️ Response status: {response.status_code}")
            if hasattr(response, 'content'):
                print(f"Content preview: {str(response.content)[:200]}...")
        
        # ตรวจสอบข้อมูลที่บันทึก
        print("\n=== ตรวจสอบข้อมูลหลังบันทึก ===")
        
        # ดูเครื่องมือที่ใช้สอบเทียบ
        equipment_used = CalibrationEquipmentUsed.objects.filter(
            calibration_type='pressure',
            calibration_id=pressure.cal_pressure_id
        )
        print(f"✅ เครื่องมือที่ใช้สอบเทียบ: {equipment_used.count()} ตัว")
        
        for eq in equipment_used:
            print(f"  - {eq.equipment.name} (ID: {eq.equipment.id})")
        
        # ดูข้อมูล Pressure ที่อัปเดต
        updated_pressure = CalibrationPressure.objects.get(cal_pressure_id=pressure.cal_pressure_id)
        print(f"✅ สถานะ Pressure: {updated_pressure.status}")
        print(f"✅ เครื่องมือหลัก: {updated_pressure.std_id}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_pressure_form_with_equipment()
