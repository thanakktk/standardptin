from django import forms
from .models import CalibrationPressure, CalibrationTorque, DialGaugeCalibration, DialGaugeReading, BalanceCalibration, BalanceReading, MicrowaveCalibration, MicrowaveReading, HighFrequencyCalibration, LowFrequencyCalibration
from django.contrib.auth import get_user_model
from machine.models import Machine, MachineType, CalibrationEquipment
from std.models import Standard


class CalibrationPressureForm(forms.ModelForm):
    class Meta:
        model = CalibrationPressure
        fields = ['measurement_range', 'set', 'm1', 'm2', 'm3', 'm4', 'avg', 'actual', 'error', 'tolerance_start', 'tolerance_end', 'update', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number',
                 'set_2', 'm1_2', 'm2_2', 'm3_2', 'm4_2', 'avg_2', 'actual_2', 'error_2', 'tolerance_start_2', 'tolerance_end_2',
                 'set_3', 'm1_3', 'm2_3', 'm3_3', 'm4_3', 'avg_3', 'actual_3', 'error_3', 'tolerance_start_3', 'tolerance_end_3',
                 'set_4', 'm1_4', 'm2_4', 'm3_4', 'm4_4', 'avg_4', 'actual_4', 'error_4', 'tolerance_start_4', 'tolerance_end_4',
                 'set_5', 'm1_5', 'm2_5', 'm3_5', 'm4_5', 'avg_5', 'actual_5', 'error_5', 'tolerance_start_5', 'tolerance_end_5',
                 'set_6', 'm1_6', 'm2_6', 'm3_6', 'm4_6', 'avg_6', 'actual_6', 'error_6', 'tolerance_start_6', 'tolerance_end_6']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 bar'}),
            'set': forms.TextInput(attrs={'class': 'form-control'}),
            'm1': forms.TextInput(attrs={'class': 'form-control'}),
            'm2': forms.TextInput(attrs={'class': 'form-control'}),
            'm3': forms.TextInput(attrs={'class': 'form-control'}),
            'm4': forms.TextInput(attrs={'class': 'form-control'}),
            'avg': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'actual': forms.NumberInput(attrs={'class': 'form-control'}),
            'error': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_start': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_end': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            # ฟิลด์สำหรับแถวที่ 2-6
            'actual_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'error_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_start_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_end_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'actual_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'error_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_start_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_end_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'actual_4': forms.NumberInput(attrs={'class': 'form-control'}),
            'error_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_start_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_end_4': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'actual_5': forms.NumberInput(attrs={'class': 'form-control'}),
            'error_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_start_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_end_5': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'actual_6': forms.NumberInput(attrs={'class': 'form-control'}),
            'error_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_start_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_end_6': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
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
        fields = ['measurement_range', 'cwset', 'cw0', 'cw90', 'cw180', 'cw270', 'cw_reading', 'cw_avg', 'cw_actual', 'cw_error', 'cw_tolerance_start', 'cw_tolerance_end', 
                 'ccwset', 'ccw0', 'ccw90', 'ccw180', 'ccw270', 'ccw_reading', 'ccw_avg', 'ccw_actual', 'ccw_error', 'ccw_tolerance_start', 'ccw_tolerance_end',
                 'cwset_2', 'cw_actual_2', 'cw_error_2', 'cw_tolerance_start_2', 'cw_tolerance_end_2',
                 'ccwset_2', 'ccw_actual_2', 'ccw_error_2', 'ccw_tolerance_start_2', 'ccw_tolerance_end_2',
                 'cwset_3', 'cw_actual_3', 'cw_error_3', 'cw_tolerance_start_3', 'cw_tolerance_end_3',
                 'ccwset_3', 'ccw_actual_3', 'ccw_error_3', 'ccw_tolerance_start_3', 'ccw_tolerance_end_3',
                 'update', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 bar'}),
            'cwset': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw0': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw90': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw180': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw270': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_reading': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_avg': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_actual': forms.NumberInput(attrs={'class': 'form-control'}),
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
            'ccw_actual': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_error': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_tolerance_start': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_tolerance_end': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # ฟิลด์สำหรับแถวที่ 2
            'cwset_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_actual_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_error_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_tolerance_start_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_tolerance_end_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccwset_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_actual_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_error_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_tolerance_start_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_tolerance_end_2': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # ฟิลด์สำหรับแถวที่ 3
            'cwset_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_actual_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_error_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_tolerance_start_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_tolerance_end_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccwset_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_actual_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_error_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_tolerance_start_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_tolerance_end_3': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
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
    class Meta:
        model = DialGaugeCalibration
        fields = ['measurement_range', 'update', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer',
                  'uuc_set', 'actual', 'error', 'tolerance_limit',
                  'set_2', 'actual_2', 'error_2', 'tolerance_limit_2',
                  'set_3', 'actual_3', 'error_3', 'tolerance_limit_3',
                  'set_4', 'actual_4', 'error_4', 'tolerance_limit_4',
                  'set_5', 'actual_5', 'error_5', 'tolerance_limit_5']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 inch'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'uuc_set': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.1000'}),
            'actual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.1005'}),
            'error': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 2
            'set_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.1000'}),
            'actual_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.1005'}),
            'error_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 3
            'set_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.2000'}),
            'actual_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.2003'}),
            'error_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 4
            'set_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.3000'}),
            'actual_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.3001'}),
            'error_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 5
            'set_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.4000'}),
            'actual_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.4002'}),
            'error_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
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

class DialGaugeReadingForm(forms.ModelForm):
    class Meta:
        model = DialGaugeReading
        fields = ['uuc_set', 'std_read_up1', 'std_read_down1', 'std_read_up2', 'std_read_down2', 'average_up', 'average_down', 'error']
        widgets = {
            'uuc_set': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_up1': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_down1': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_up2': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_down2': forms.NumberInput(attrs={'class': 'form-control'}),
            'average_up': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'average_down': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'error': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class BalanceCalibrationForm(forms.ModelForm):
    class Meta:
        model = BalanceCalibration
        fields = ['measurement_range', 'update', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number',
                  'linear_nominal_value', 'linear_conventional_mass', 'linear_displayed_value', 'linear_error', 'linear_uncertainty',
                  'linear_nominal_value_2', 'linear_conventional_mass_2', 'linear_displayed_value_2', 'linear_error_2', 'linear_uncertainty_2',
                  'linear_nominal_value_3', 'linear_conventional_mass_3', 'linear_displayed_value_3', 'linear_error_3', 'linear_uncertainty_3',
                  'linear_nominal_value_4', 'linear_conventional_mass_4', 'linear_displayed_value_4', 'linear_error_4', 'linear_uncertainty_4',
                  'linear_nominal_value_5', 'linear_conventional_mass_5', 'linear_displayed_value_5', 'linear_error_5', 'linear_uncertainty_5']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 g'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            # Row 1
            'linear_nominal_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000'}),
            'linear_conventional_mass': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000'}),
            'linear_displayed_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.00002'}),
            'linear_error': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'linear_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 2
            'linear_nominal_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000'}),
            'linear_conventional_mass_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000'}),
            'linear_displayed_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.00003'}),
            'linear_error_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'linear_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 3
            'linear_nominal_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000'}),
            'linear_conventional_mass_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000'}),
            'linear_displayed_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.00005'}),
            'linear_error_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'linear_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 4
            'linear_nominal_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100.0000'}),
            'linear_conventional_mass_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100.0000'}),
            'linear_displayed_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100.00008'}),
            'linear_error_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'linear_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 5
            'linear_nominal_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200.0000'}),
            'linear_conventional_mass_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200.0000'}),
            'linear_displayed_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200.00010'}),
            'linear_error_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'linear_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
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

class BalanceReadingForm(forms.ModelForm):
    class Meta:
        model = BalanceReading
        fields = ['uuc_set', 'std_read_1', 'std_read_2', 'std_read_3', 'std_read_4', 'std_read_5', 'std_read_6', 'std_read_7', 'std_read_8', 'std_read_9', 'std_read_10']
        widgets = {
            'uuc_set': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_4': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_5': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_6': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_7': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_8': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_9': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_read_10': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MicrowaveCalibrationForm(forms.ModelForm):
    class Meta:
        model = MicrowaveCalibration
        fields = ['update', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number']
        widgets = {
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

class MicrowaveReadingForm(forms.ModelForm):
    class Meta:
        model = MicrowaveReading
        fields = ['test_type', 'function_test', 'nominal_value', 'rf_level', 'frequency', 'measured_value', 'unit', 'uncertainty', 'tolerance_limit_min', 'tolerance_limit_max', 'test_result']
        widgets = {
            'test_type': forms.Select(attrs={'class': 'form-control'}),
            'function_test': forms.TextInput(attrs={'class': 'form-control'}),
            'nominal_value': forms.TextInput(attrs={'class': 'form-control'}),
            'rf_level': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'measured_value': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'uncertainty': forms.NumberInput(attrs={'class': 'form-control'}),
            'tolerance_limit_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'tolerance_limit_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'test_result': forms.Select(attrs={'class': 'form-control'}),
        }

class HighFrequencyCalibrationForm(forms.ModelForm):
    class Meta:
        model = HighFrequencyCalibration
        fields = ['next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number']
        widgets = {
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

class LowFrequencyCalibrationForm(forms.ModelForm):
    class Meta:
        model = LowFrequencyCalibration
        fields = ['next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number']
        widgets = {
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