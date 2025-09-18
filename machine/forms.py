from django import forms
from .models import Machine, MachineType, MachineUnit, Manufacture, CalibrationEquipment
from django.db.models import Q
from datetime import datetime

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['organize', 'machine_type', 'name', 'model', 'serial_number', 'range', 'res_uuc', 'unit', 'manufacture']
        widgets = {
            'organize': forms.Select(attrs={'class': 'form-control'}),
            'machine_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'range': forms.TextInput(attrs={'class': 'form-control'}),
            'res_uuc': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'manufacture': forms.Select(attrs={'class': 'form-control'}),
        }

class SendMachineEmailForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), required=False)

class MachineFilterForm(forms.Form):
    # ฟิลเตอร์สำหรับหน่วยงาน
    organize_id = forms.IntegerField(
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'รหัสหน่วยงาน'})
    )
    
    # ฟิลเตอร์สำหรับประเภทเครื่องมือ
    machine_type = forms.ModelChoiceField(
        queryset=MachineType.objects.all(),
        required=False,
        empty_label="เลือกประเภทเครื่องมือ",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # ฟิลเตอร์สำหรับวันที่
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    
    # ค้นหา Serial Number
    serial_search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ค้นหา Serial Number'})
    )
    
    # ค้นหาชื่อเครื่องมือ
    name_search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ค้นหาชื่อเครื่องมือ'})
    )
    
    # ฟิลเตอร์สำหรับสถานะ
    status = forms.ChoiceField(
        choices=[('', 'เลือกสถานะ')] + Machine.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class CalibrationDataForm(forms.Form):
    # ข้อมูลสำหรับบันทึกการสอบเทียบ
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    model = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    serial_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    max_value = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    measurement_range = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    resolution = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    uuc_unit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    unit_count = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    organization = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    manufacturer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    calculator = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class CalibrationEquipmentForm(forms.ModelForm):
    class Meta:
        model = CalibrationEquipment
        fields = ['name', 'model', 'serial_number', 'certificate', 'machine_type', 'created_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'กรอกเลขที่ใบรับรอง'}),
            'machine_type': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
    
    def clean_created_at(self):
        from django.utils import timezone
        created_at = self.cleaned_data.get('created_at')
        
        # ถ้าไม่กรอก ให้ใช้เวลาปัจจุบัน
        if not created_at:
            return timezone.now()
        
        # ตรวจสอบว่าไม่ใช่วันอนาคต
        if created_at > timezone.now():
            raise forms.ValidationError("วันที่สร้างไม่สามารถเป็นวันอนาคตได้")
        
        return created_at 