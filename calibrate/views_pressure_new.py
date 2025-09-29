"""
New Pressure Views - ยึด Low Frequency เป็นหลัก
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from calibrate.models import CalibrationPressure, CalibrationEquipmentUsed
from calibrate.forms import CalibrationPressureForm


class CalibrationPressureUpdateViewNew(LoginRequiredMixin, UpdateView):
    """แก้ไขการสอบเทียบ Pressure - ใช้ template ใหม่"""
    model = CalibrationPressure
    form_class = CalibrationPressureForm
    template_name = 'calibrate/pressure_form_new.html'
    success_url = reverse_lazy('calibrate-dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'แก้ไขการสอบเทียบ Pressure - {self.object.uuc_id.name}'
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == 'POST':
            # ตั้งค่า default value สำหรับ status ถ้าไม่ได้ส่งมา
            if 'status' not in self.request.POST:
                kwargs['data'] = kwargs.get('data', {}).copy()
                kwargs['data']['status'] = 'in_progress'
        return kwargs
    
    def form_invalid(self, form):
        print("=== DEBUG: Form is invalid ===")
        print(f"Form errors: {form.errors}")
        print(f"Form non_field_errors: {form.non_field_errors()}")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        print("=== DEBUG: ก่อนบันทึก Pressure New ===")
        print(f"POST data: {dict(self.request.POST)}")
        print(f"Form is_valid: {form.is_valid()}")
        print(f"Form cleaned_data: {form.cleaned_data}")
        print(f"Object ID: {self.object.cal_pressure_id if self.object else 'None'}")
        print(f"Request method: {self.request.method}")
        print(f"Request user: {self.request.user}")
        
        # ตรวจสอบ form errors
        if form.errors:
            print(f"❌ Form errors: {form.errors}")
            return self.form_invalid(form)
        
        # ตรวจสอบ required fields
        required_fields = ['measurement_range', 'update', 'next_due']
        for field in required_fields:
            if field in form.cleaned_data and form.cleaned_data[field]:
                print(f"✅ {field}: {form.cleaned_data[field]}")
            else:
                print(f"⚠️ {field}: {form.cleaned_data.get(field, 'MISSING')}")
        
        # ตรวจสอบ measurement_range fields
        for i in range(2, 7):
            field_name = f'measurement_range_{i}'
            if field_name in self.request.POST:
                print(f"📝 {field_name}: {self.request.POST[field_name]}")
        
        # ตรวจสอบ equipment data
        print(f"=== DEBUG: Equipment data ===")
        print(f"std_id: {self.request.POST.get('std_id', 'NOT FOUND')}")
        print(f"selected_equipment: {self.request.POST.get('selected_equipment', 'NOT FOUND')}")
        for key, value in self.request.POST.items():
            if 'std_id' in key:
                print(f"Equipment field {key}: {value}")
        
        # บันทึกข้อมูลการสอบเทียบ
        calibration = form.save()
        print(f"✅ บันทึก calibration ID: {calibration.cal_pressure_id}")
        
        # Debug: ดูข้อมูลที่ส่งมา
        print(f"=== DEBUG: POST data for equipment (Pressure New) ===")
        for key, value in self.request.POST.items():
            if 'std_id' in key:
                print(f"{key}: {value}")
        
        # รวบรวมเครื่องมือทั้งหมดที่จะบันทึก
        equipment_ids = []
        
        # 1. จัดการข้อมูลเครื่องมือจาก selected_equipment
        selected_equipment = self.request.POST.get('selected_equipment', '')
        print(f"=== DEBUG: selected_equipment = '{selected_equipment}'")
        if selected_equipment:
            equipment_ids.extend([eid.strip() for eid in selected_equipment.split(',') if eid.strip()])
        
        # 2. จัดการข้อมูลเครื่องมือจาก form field หลัก (std_id)
        std_id_value = self.request.POST.get('std_id', '')
        if std_id_value:
            equipment_ids.append(std_id_value)
        
        # 3. จัดการข้อมูลเครื่องมือจาก form fields (std_id_*)
        for key, value in self.request.POST.items():
            if key.startswith('std_id_') and value and not key.startswith('std_id_existing_'):
                equipment_ids.append(value)
        
        # 4. จัดการข้อมูลเครื่องมือที่มีอยู่แล้ว (std_id_existing_*)
        for key, value in self.request.POST.items():
            if key.startswith('std_id_existing_') and value:
                equipment_ids.append(value)
        
        # ลบ duplicate equipment IDs
        equipment_ids = list(set(equipment_ids))
        print(f"=== DEBUG: Final equipment_ids (unique) = {equipment_ids}")
        
        # ลบเครื่องมือเก่าทั้งหมด
        CalibrationEquipmentUsed.objects.filter(
            calibration_type='pressure',
            calibration_id=calibration.cal_pressure_id
        ).delete()
        
        # บันทึกเครื่องมือใหม่ทั้งหมด
        for equipment_id in equipment_ids:
            try:
                from machine.models import CalibrationEquipment
                equipment = CalibrationEquipment.objects.get(id=equipment_id)
                
                # ตรวจสอบว่ามีอยู่แล้วหรือไม่
                existing = CalibrationEquipmentUsed.objects.filter(
                    calibration_type='pressure',
                    calibration_id=calibration.cal_pressure_id,
                    equipment=equipment
                ).exists()
                
                if not existing:
                    CalibrationEquipmentUsed.objects.create(
                        calibration_type='pressure',
                        calibration_id=calibration.cal_pressure_id,
                        equipment=equipment
                    )
                    print(f"=== DEBUG: Saved equipment {equipment.name} (ID: {equipment_id})")
                else:
                    print(f"=== DEBUG: Equipment {equipment.name} (ID: {equipment_id}) already exists, skipping")
                    
            except CalibrationEquipment.DoesNotExist:
                print(f"=== DEBUG: Equipment ID {equipment_id} not found")
                continue
        
        # ตรวจสอบสถานะอัตโนมัติ
        self.auto_check_status(calibration)
        
        # เพิ่ม success message
        messages.success(self.request, 'บันทึกการสอบเทียบ Pressure เรียบร้อยแล้ว')
        
        print("✅ บันทึกสำเร็จ! จะ redirect ไปแล้ว")
        
        # ให้ Django จัดการ redirect ตาม success_url
        return super().form_valid(form)
    
    def auto_check_status(self, calibration):
        """ตรวจสอบสถานะอัตโนมัติสำหรับ Pressure"""
        # ตรวจสอบว่ามีข้อมูลครบถ้วนหรือไม่
        has_data = any([
            calibration.set, calibration.actual,
            calibration.set_2, calibration.actual_2,
            calibration.set_3, calibration.actual_3
        ])
        
        if not has_data:
            # ยังไม่มีข้อมูล = กำลังสอบเทียบ
            calibration.status = 'in_progress'
        else:
            # มีข้อมูลแล้ว = ตรวจสอบผลการสอบเทียบ
            if self.check_pressure_pass_fail(calibration):
                calibration.status = 'passed'
            else:
                calibration.status = 'failed'
        
        calibration.save()
    
    def check_pressure_pass_fail(self, calibration):
        """ตรวจสอบผลการสอบเทียบ Pressure"""
        # ตรวจสอบ tolerance สำหรับแต่ละแถว
        rows_to_check = [
            (calibration.set, calibration.actual, calibration.tolerance_start, calibration.tolerance_end),
            (calibration.set_2, calibration.actual_2, calibration.tolerance_start_2, calibration.tolerance_end_2),
            (calibration.set_3, calibration.actual_3, calibration.tolerance_start_3, calibration.tolerance_end_3),
            (calibration.set_4, calibration.actual_4, calibration.tolerance_start_4, calibration.tolerance_end_4),
            (calibration.set_5, calibration.actual_5, calibration.tolerance_start_5, calibration.tolerance_end_5),
            (calibration.set_6, calibration.actual_6, calibration.tolerance_start_6, calibration.tolerance_end_6),
        ]
        
        for set_val, actual_val, tolerance_start, tolerance_end in rows_to_check:
            if set_val and actual_val and tolerance_start and tolerance_end:
                if not (tolerance_start <= actual_val <= tolerance_end):
                    return False
        
        return True
