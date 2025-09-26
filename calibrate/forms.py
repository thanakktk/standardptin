from django import forms
from .models import CalibrationPressure, CalibrationTorque, DialGaugeCalibration, DialGaugeReading, BalanceCalibration, BalanceReading, MicrowaveCalibration, MicrowaveReading, HighFrequencyCalibration, LowFrequencyCalibration
from django.contrib.auth import get_user_model
from machine.models import Machine, MachineType, CalibrationEquipment
from std.models import Standard


class CalibrationPressureForm(forms.ModelForm):
    class Meta:
        model = CalibrationPressure
        fields = ['measurement_range', 'set', 'm1', 'm2', 'm3', 'm4', 'avg', 'error', 'tolerance_start', 'tolerance_end', 'update', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number',
                 'set_2', 'm1_2', 'm2_2', 'm3_2', 'm4_2', 'avg_2', 'error_2',
                 'set_3', 'm1_3', 'm2_3', 'm3_3', 'm4_3', 'avg_3', 'error_3',
                 'set_4', 'm1_4', 'm2_4', 'm3_4', 'm4_4', 'avg_4', 'error_4',
                 'set_5', 'm1_5', 'm2_5', 'm3_5', 'm4_5', 'avg_5', 'error_5',
                 'set_6', 'm1_6', 'm2_6', 'm3_6', 'm4_6', 'avg_6', 'error_6']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 bar'}),
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
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        # ลบการตั้งค่า uuc_id เพราะเราใช้ std_id แทน
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class CalibrationTorqueForm(forms.ModelForm):
    class Meta:
        model = CalibrationTorque
        fields = ['cwset', 'cw0', 'cw90', 'cw180', 'cw270', 'cw_reading', 'cw_avg', 'cw_error', 'cw_tolerance_start', 'cw_tolerance_end', 'ccwset', 'ccw0', 'ccw90', 'ccw180', 'ccw270', 'ccw_reading', 'ccw_avg', 'ccw_error', 'ccw_tolerance_start', 'ccw_tolerance_end', 'update', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number']
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
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class DialGaugeCalibrationForm(forms.ModelForm):
    """ฟอร์มสำหรับการสอบเทียบ Dial Gauge"""
    class Meta:
        model = DialGaugeCalibration
        fields = ['machine', 'std_id', 'calibrator', 'certificate_issuer', 'date_calibration', 'update', 'next_due', 'res_uuc', 'acc_std', 'status', 'type_a_sd', 'type_b_res_uuc', 'type_b_acc_std', 'type_b_hysteresis', 'uc_68', 'k_factor', 'expanded_uncertainty_95',
                 'uuc_set', 'actual', 'error', 'uncertainty', 'tolerance_limit']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
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
            # Dial Gauge Calibration fields
            'uuc_set': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0050'}),
            'actual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0050'}),
            'error': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000'}),
            'uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0003'}),
            'tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0040 – 0.0060'}),
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
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

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
        fields = ['machine', 'std_id', 'calibrator', 'certificate_issuer', 'date_calibration', 'received_date', 'issue_date', 'next_due', 'certificate_number', 'procedure_number', 'status',
                 'linear_nominal_value', 'linear_conventional_mass', 'linear_displayed_value', 'linear_error', 'linear_uncertainty', 'linear_tolerance_limit']
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
            # Linear (Min-Max) fields
            'linear_nominal_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000'}),
            'linear_conventional_mass': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000'}),
            'linear_displayed_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.00002'}),
            'linear_error': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'linear_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.00003'}),
            'linear_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
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
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

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
        fields = ['machine', 'std_id', 'calibrator', 'certificate_issuer', 'date_calibration', 'update', 'next_due', 'certificate_number', 'status',
                 'dc_uuc_range', 'dc_uuc_setting', 'dc_measured_value', 'dc_uncertainty', 'dc_tolerance_limit']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'date_calibration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            # DC VOLTAGE fields
            'dc_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 962 MHz'}),
            'dc_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -2 dBm'}),
            'dc_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 961.9922 MHz'}),
            'dc_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -0.0078 MHz'}),
            'dc_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 961.9000 – 962.1000 MHz'}),
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
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

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

class HighFrequencyCalibrationForm(forms.ModelForm):
    class Meta:
        model = HighFrequencyCalibration
        fields = ['machine', 'std_id', 'calibrator', 'certificate_issuer', 'date_calibration', 'next_due', 'certificate_number', 'status', 'priority',
                 'freq_uuc_range', 'freq_uuc_setting', 'freq_measured_value', 'freq_uncertainty', 'freq_tolerance_limit',
                 'freq_uuc_range_2', 'freq_uuc_setting_2', 'freq_measured_value_2', 'freq_uncertainty_2', 'freq_tolerance_limit_2',
                 'freq_uuc_range_3', 'freq_uuc_setting_3', 'freq_measured_value_3', 'freq_uncertainty_3', 'freq_tolerance_limit_3',
                 'freq_uuc_range_4', 'freq_uuc_setting_4', 'freq_measured_value_4', 'freq_uncertainty_4', 'freq_tolerance_limit_4',
                 'freq_uuc_range_5', 'freq_uuc_setting_5', 'freq_measured_value_5', 'freq_uncertainty_5', 'freq_tolerance_limit_5',
                 'volt_uuc_range', 'volt_uuc_setting', 'volt_measured_value', 'volt_uncertainty', 'volt_tolerance_limit',
                 'volt_uuc_range_2', 'volt_uuc_setting_2', 'volt_measured_value_2', 'volt_uncertainty_2', 'volt_tolerance_limit_2',
                 'volt_uuc_range_3', 'volt_uuc_setting_3', 'volt_measured_value_3', 'volt_uncertainty_3', 'volt_tolerance_limit_3',
                 'volt_uuc_range_4', 'volt_uuc_setting_4', 'volt_measured_value_4', 'volt_uncertainty_4', 'volt_tolerance_limit_4',
                 'volt_uuc_range_5', 'volt_uuc_setting_5', 'volt_measured_value_5', 'volt_uncertainty_5', 'volt_tolerance_limit_5']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'date_calibration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            # Frequency fields
            'freq_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 MHz'}),
            'freq_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 MHz'}),
            'freq_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 MHz'}),
            'freq_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 MHz'}),
            'freq_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 9.0085 – 10.0015 MHz'}),
            # Frequency fields row 2
            'freq_uuc_range_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20 MHz'}),
            'freq_uuc_setting_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 MHz'}),
            'freq_measured_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 MHz'}),
            'freq_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 MHz'}),
            'freq_tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 19.0085 – 20.0015 MHz'}),
            # Frequency fields row 3
            'freq_uuc_range_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 MHz'}),
            'freq_uuc_setting_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 MHz'}),
            'freq_measured_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 MHz'}),
            'freq_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 MHz'}),
            'freq_tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 49.0085 – 50.0015 MHz'}),
            # Frequency fields row 4
            'freq_uuc_range_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 MHz'}),
            'freq_uuc_setting_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100.0000 MHz'}),
            'freq_measured_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100.0000 MHz'}),
            'freq_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 MHz'}),
            'freq_tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 99.0085 – 100.0015 MHz'}),
            # Frequency fields row 5
            'freq_uuc_range_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 MHz'}),
            'freq_uuc_setting_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200.0000 MHz'}),
            'freq_measured_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200.0000 MHz'}),
            'freq_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 MHz'}),
            'freq_tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 199.0085 – 200.0015 MHz'}),
            # Voltage fields
            'volt_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 VDC'}),
            'volt_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1.0000 V'}),
            'volt_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1.0001 V'}),
            'volt_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -0.0001 V'}),
            'volt_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.9997 – 1.0007 V'}),
            # Voltage fields row 2
            'volt_uuc_range_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20 VDC'}),
            'volt_uuc_setting_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 2.0000 V'}),
            'volt_measured_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 2.0001 V'}),
            'volt_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -0.0001 V'}),
            'volt_tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1.9997 – 2.0007 V'}),
            # Voltage fields row 3
            'volt_uuc_range_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 VDC'}),
            'volt_uuc_setting_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 5.0000 V'}),
            'volt_measured_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 5.0001 V'}),
            'volt_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -0.0001 V'}),
            'volt_tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 4.9997 – 5.0007 V'}),
            # Voltage fields row 4
            'volt_uuc_range_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 VDC'}),
            'volt_uuc_setting_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 V'}),
            'volt_measured_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0001 V'}),
            'volt_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -0.0001 V'}),
            'volt_tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 9.9997 – 10.0007 V'}),
            # Voltage fields row 5
            'volt_uuc_range_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 VDC'}),
            'volt_uuc_setting_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 V'}),
            'volt_measured_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0001 V'}),
            'volt_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -0.0001 V'}),
            'volt_tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 19.9997 – 20.0007 V'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"
        
        # ตั้งค่า queryset สำหรับเครื่องมือ High Frequency
        high_freq_type = MachineType.objects.filter(name__icontains='high frequency').first()
        if high_freq_type:
            self.fields['machine'].queryset = Machine.objects.filter(machine_type=high_freq_type, deleted=False).order_by('name')
        else:
            self.fields['machine'].queryset = Machine.objects.filter(deleted=False).order_by('name')
        self.fields['machine'].empty_label = "เลือกเครื่องมือ High Frequency"

class LowFrequencyCalibrationForm(forms.ModelForm):
    class Meta:
        model = LowFrequencyCalibration
        fields = ['machine', 'std_id', 'calibrator', 'certificate_issuer', 'date_calibration', 'next_due', 'certificate_number', 'status', 'priority',
                 'dc_uuc_range', 'dc_uuc_setting', 'dc_measured_value', 'dc_uncertainty', 'dc_tolerance_limit', 'dc_error', 'dc_pass_fail', 'dc_remarks',
                 'ac_uuc_range', 'ac_uuc_setting', 'ac_measured_value', 'ac_uncertainty', 'ac_tolerance_limit', 'ac_error', 'ac_pass_fail', 'ac_remarks',
                 'res_uuc_range', 'res_uuc_setting', 'res_measured_value', 'res_uncertainty', 'res_tolerance_limit', 'res_error', 'res_pass_fail', 'res_remarks']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'date_calibration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            # DC Voltage fields
            'dc_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 mV'}),
            'dc_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 49.0035 – 50.0065 mV'}),
            'dc_error': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 mV'}),
            'dc_pass_fail': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'เลือก'), ('pass', 'ผ่าน'), ('fail', 'ไม่ผ่าน')]),
            'dc_remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'หมายเหตุ...'}),
            # AC Voltage fields
            'ac_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'ac_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'ac_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'ac_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 mV'}),
            'ac_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 45.0080 – 50.0020 mV'}),
            'ac_error': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 mV'}),
            'ac_pass_fail': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'เลือก'), ('pass', 'ผ่าน'), ('fail', 'ไม่ผ่าน')]),
            'ac_remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'หมายเหตุ...'}),
            # Resistance fields
            'res_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 Ω'}),
            'res_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 Ω'}),
            'res_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 Ω'}),
            'res_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 Ω'}),
            'res_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 499.0077 – 500.0033 Ω'}),
            'res_error': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 Ω'}),
            'res_pass_fail': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'เลือก'), ('pass', 'ผ่าน'), ('fail', 'ไม่ผ่าน')]),
            'res_remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'หมายเหตุ...'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"
