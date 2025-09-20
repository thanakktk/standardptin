from django import forms
from .models import CalibrationForce, CalibrationPressure, CalibrationTorque, DialGaugeCalibration, DialGaugeReading, BalanceCalibration, BalanceReading, MicrowaveCalibration, MicrowaveReading
from django.contrib.auth import get_user_model
from machine.models import Machine, MachineType
from std.models import Standard

class CalibrationForceForm(forms.ModelForm):
    class Meta:
        model = CalibrationForce
        fields = ['apply_com', 'apply_ten', 'compress', 'tension', 'fullscale', 'error', 'tolerance_start', 'tolerance_end', 'update', 'next_due', 'status', 'uuc_id', 'std_id', 'calibrator', 'certificate_issuer']
        widgets = {
            'apply_com': forms.TextInput(attrs={'class': 'form-control'}),
            'apply_ten': forms.TextInput(attrs={'class': 'form-control'}),
            'compress': forms.TextInput(attrs={'class': 'form-control'}),
            'tension': forms.TextInput(attrs={'class': 'form-control'}),
            'fullscale': forms.NumberInput(attrs={'class': 'form-control'}),
            'error': forms.NumberInput(attrs={'class': 'form-control'}),
            'tolerance_start': forms.NumberInput(attrs={'class': 'form-control'}),
            'tolerance_end': forms.NumberInput(attrs={'class': 'form-control'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'uuc_id': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือการสอบเทียบ
        self.fields['std_id'].queryset = Standard.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือการสอบเทียบ"

class CalibrationPressureForm(forms.ModelForm):
    class Meta:
        model = CalibrationPressure
        fields = ['set', 'm1', 'm2', 'm3', 'm4', 'avg', 'error', 'tolerance_start', 'tolerance_end', 'update', 'next_due', 'status', 'uuc_id', 'std_id', 'calibrator', 'certificate_issuer']
        widgets = {
            'set': forms.TextInput(attrs={'class': 'form-control'}),
            'm1': forms.TextInput(attrs={'class': 'form-control'}),
            'm2': forms.TextInput(attrs={'class': 'form-control'}),
            'm3': forms.TextInput(attrs={'class': 'form-control'}),
            'm4': forms.TextInput(attrs={'class': 'form-control'}),
            'avg': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'error': forms.NumberInput(attrs={'class': 'form-control'}),
            'tolerance_start': forms.NumberInput(attrs={'class': 'form-control'}),
            'tolerance_end': forms.NumberInput(attrs={'class': 'form-control'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'uuc_id': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือการสอบเทียบ
        self.fields['std_id'].queryset = Standard.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือการสอบเทียบ"

class CalibrationTorqueForm(forms.ModelForm):
    class Meta:
        model = CalibrationTorque
        fields = ['cwset', 'cw0', 'cw90', 'cw180', 'cw270', 'cw_reading', 'cw_avg', 'cw_error', 'cw_tolerance_start', 'cw_tolerance_end', 'ccwset', 'ccw0', 'ccw90', 'ccw180', 'ccw270', 'ccw_reading', 'ccw_avg', 'ccw_error', 'ccw_tolerance_start', 'ccw_tolerance_end', 'update', 'next_due', 'status', 'uuc_id', 'std_id', 'calibrator', 'certificate_issuer']
        widgets = {
            'cwset': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw0': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw90': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw180': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw270': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_reading': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_avg': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_error': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_tolerance_start': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_tolerance_end': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccwset': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw0': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw90': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw180': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw270': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_reading': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_avg': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_error': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_tolerance_start': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_tolerance_end': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'uuc_id': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือการสอบเทียบ
        self.fields['std_id'].queryset = Standard.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือการสอบเทียบ"

class DialGaugeCalibrationForm(forms.ModelForm):
    """ฟอร์มสำหรับการสอบเทียบ Dial Gauge"""
    class Meta:
        model = DialGaugeCalibration
        fields = ['machine', 'std_id', 'calibrator', 'certificate_issuer', 'date_calibration', 'update', 'next_due', 'res_uuc', 'acc_std', 'status', 'type_a_sd', 'type_b_res_uuc', 'type_b_acc_std', 'type_b_hysteresis', 'uc_68', 'k_factor', 'expanded_uncertainty_95']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'date_calibration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'res_uuc': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'acc_std': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00000001'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'type_a_sd': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'type_b_res_uuc': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'type_b_acc_std': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00000001'}),
            'type_b_hysteresis': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'uc_68': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'k_factor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'expanded_uncertainty_95': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือ Dial Gauge (กรองเฉพาะประเภท Dial Gauge)
        dial_gauge_type = MachineType.objects.filter(name__icontains='dial gauge').first()
        if dial_gauge_type:
            self.fields['machine'].queryset = Machine.objects.filter(machine_type=dial_gauge_type, deleted=False).order_by('name')
        else:
            self.fields['machine'].queryset = Machine.objects.filter(deleted=False).order_by('name')
        self.fields['machine'].empty_label = "เลือก Dial Gauge"
        
        # ตั้งค่า queryset สำหรับเครื่องมือการสอบเทียบ
        self.fields['std_id'].queryset = Standard.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือการสอบเทียบ"

class DialGaugeReadingForm(forms.ModelForm):
    """ฟอร์มสำหรับข้อมูลการอ่านค่า Dial Gauge"""
    class Meta:
        model = DialGaugeReading
        fields = ['uuc_set', 'std_read_up1', 'std_read_down1', 'std_read_up2', 'std_read_down2', 'average_up', 'average_down', 'error', 'uncertainty', 'hysteresis', 'value_root2', 'value_root3', 'value_2root3']
        widgets = {
            'uuc_set': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001'}),
            'std_read_up1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'std_read_down1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'std_read_up2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'std_read_down2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'average_up': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'average_down': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'error': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'uncertainty': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'hysteresis': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'value_root2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'value_root3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'value_2root3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
        }

class BalanceCalibrationForm(forms.ModelForm):
    """ฟอร์มสำหรับการสอบเทียบ Balance"""
    class Meta:
        model = BalanceCalibration
        fields = ['machine', 'std_id', 'calibrator', 'certificate_issuer', 'date_calibration', 'received_date', 'issue_date', 'next_due', 'certificate_number', 'procedure_number', 'status', 'drift', 'res_push', 'res_tip', 'air_buoyancy', 'uncertainty_68', 'uncertainty_95_k', 'final_uncertainty']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'date_calibration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'received_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'procedure_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'drift': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'res_push': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'res_tip': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'air_buoyancy': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'uncertainty_68': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'uncertainty_95_k': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'final_uncertainty': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือ Balance (กรองเฉพาะประเภท Balance)
        balance_type = MachineType.objects.filter(name__icontains='balance').first()
        if balance_type:
            self.fields['machine'].queryset = Machine.objects.filter(machine_type=balance_type, deleted=False).order_by('name')
        else:
            self.fields['machine'].queryset = Machine.objects.filter(deleted=False).order_by('name')
        self.fields['machine'].empty_label = "เลือก Balance"
        
        # ตั้งค่า queryset สำหรับเครื่องมือการสอบเทียบ
        self.fields['std_id'].queryset = Standard.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือการสอบเทียบ"

class BalanceReadingForm(forms.ModelForm):
    """ฟอร์มสำหรับข้อมูลการอ่านค่า Balance"""
    class Meta:
        model = BalanceReading
        fields = ['uuc_set', 'std_read_1', 'std_read_2', 'std_read_3', 'std_read_4', 'std_read_5', 'std_read_6', 'std_read_7', 'std_read_8', 'std_read_9', 'std_read_10', 'average', 'standard_deviation', 'uncertainty']
        widgets = {
            'uuc_set': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001'}),
            'std_read_1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_4': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_5': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_6': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_7': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_8': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_9': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'std_read_10': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'average': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001', 'readonly': 'readonly'}),
            'standard_deviation': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001', 'readonly': 'readonly'}),
            'uncertainty': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001', 'readonly': 'readonly'}),
        }

class MicrowaveCalibrationForm(forms.ModelForm):
    """ฟอร์มสำหรับการสอบเทียบ Microwave"""
    class Meta:
        model = MicrowaveCalibration
        fields = ['machine', 'std_id', 'calibrator', 'certificate_issuer', 'date_calibration', 'update', 'next_due', 'certificate_number', 'status']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'date_calibration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือ Microwave (กรองเฉพาะประเภท Microwave)
        microwave_type = MachineType.objects.filter(name__icontains='microwave').first()
        if microwave_type:
            self.fields['machine'].queryset = Machine.objects.filter(machine_type=microwave_type, deleted=False).order_by('name')
        else:
            self.fields['machine'].queryset = Machine.objects.filter(deleted=False).order_by('name')
        self.fields['machine'].empty_label = "เลือก Microwave"
        
        # ตั้งค่า queryset สำหรับเครื่องมือการสอบเทียบ
        self.fields['std_id'].queryset = Standard.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือการสอบเทียบ"

class MicrowaveReadingForm(forms.ModelForm):
    """ฟอร์มสำหรับข้อมูลการอ่านค่า Microwave"""
    class Meta:
        model = MicrowaveReading
        fields = ['test_type', 'function_test', 'nominal_value', 'rf_level', 'frequency', 'measured_value', 'measured_value_numeric', 'unit', 'uncertainty', 'tolerance_limit_min', 'tolerance_limit_max', 'test_result', 'notes']
        widgets = {
            'test_type': forms.Select(attrs={'class': 'form-control'}),
            'function_test': forms.TextInput(attrs={'class': 'form-control'}),
            'nominal_value': forms.TextInput(attrs={'class': 'form-control'}),
            'rf_level': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'measured_value': forms.TextInput(attrs={'class': 'form-control'}),
            'measured_value_numeric': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'uncertainty': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'tolerance_limit_min': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'tolerance_limit_max': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'test_result': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
