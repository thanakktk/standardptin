from django import forms
from django.contrib.auth import get_user_model
from .models import (
    CalibrationPressure, CalibrationTorque, BalanceCalibration, 
    HighFrequencyCalibration, LowFrequencyCalibration, MicrowaveCalibration, DialGaugeCalibration
)

class CalibrationPressureForm(forms.ModelForm):
    class Meta:
        model = CalibrationPressure
        fields = ['measurement_range', 'set', 'm1', 'm2', 'm3', 'm4', 'actual', 'error', 'tolerance_start', 'tolerance_end',
                  'set_2', 'm1_2', 'm2_2', 'm3_2', 'm4_2', 'actual_2', 'error_2', 'tolerance_start_2', 'tolerance_end_2',
                  'set_3', 'm1_3', 'm2_3', 'm3_3', 'm4_3', 'actual_3', 'error_3', 'tolerance_start_3', 'tolerance_end_3',
                  'set_4', 'm1_4', 'm2_4', 'm3_4', 'm4_4', 'actual_4', 'error_4', 'tolerance_start_4', 'tolerance_end_4',
                  'set_5', 'm1_5', 'm2_5', 'm3_5', 'm4_5', 'actual_5', 'error_5', 'tolerance_start_5', 'tolerance_end_5',
                  'set_6', 'm1_6', 'm2_6', 'm3_6', 'm4_6', 'actual_6', 'error_6', 'tolerance_start_6', 'tolerance_end_6',
                  'std_id', 'calibrator', 'certificate_issuer', 'certificate_number', 'status', 'priority']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 bar'}),
            'set': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 bar'}),
            'm1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'actual': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar', 'step': '0.0001'}),
            'error': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_start': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 9.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_end': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'set_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20 bar'}),
            'm1_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 bar'}),
            'm2_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 bar'}),
            'm3_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 bar'}),
            'm4_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 bar'}),
            'actual_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 bar', 'step': '0.0001'}),
            'error_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_start_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 19.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_end_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'set_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30 bar'}),
            'm1_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 bar'}),
            'm2_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 bar'}),
            'm3_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 bar'}),
            'm4_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 bar'}),
            'actual_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 bar', 'step': '0.0001'}),
            'error_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_start_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 29.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_end_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'set_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40 bar'}),
            'm1_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 bar'}),
            'm2_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 bar'}),
            'm3_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 bar'}),
            'm4_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 bar'}),
            'actual_4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 bar', 'step': '0.0001'}),
            'error_4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_start_4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 39.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_end_4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'set_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 bar'}),
            'm1_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 bar'}),
            'm2_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 bar'}),
            'm3_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 bar'}),
            'm4_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 bar'}),
            'actual_5': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 bar', 'step': '0.0001'}),
            'error_5': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_start_5': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 49.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_end_5': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'set_6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 60 bar'}),
            'm1_6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 60.0000 bar'}),
            'm2_6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 60.0000 bar'}),
            'm3_6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 60.0000 bar'}),
            'm4_6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 60.0000 bar'}),
            'actual_6': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 60.0000 bar', 'step': '0.0001'}),
            'error_6': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_start_6': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 59.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'tolerance_end_6': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 60.5000 bar', 'step': '0.0001', 'readonly': 'readonly'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class CalibrationTorqueForm(forms.ModelForm):
    class Meta:
        model = CalibrationTorque
        fields = ['measurement_range', 'cwset', 'cw0', 'cw90', 'cw180', 'cw270', 'ccwset', 'ccw0', 'ccw90', 'ccw180', 'ccw270', 
                  'cw_actual', 'cw_error', 'cw_tolerance_start', 'cw_tolerance_end',
                 'cwset_2', 'cw_actual_2', 'cw_error_2', 'cw_tolerance_start_2', 'cw_tolerance_end_2',
                  'cwset_3', 'cw_actual_3', 'cw_error_3', 'cw_tolerance_start_3', 'cw_tolerance_end_3',
                  'ccw_actual', 'ccw_error', 'ccw_tolerance_start', 'ccw_tolerance_end',
                 'ccwset_2', 'ccw_actual_2', 'ccw_error_2', 'ccw_tolerance_start_2', 'ccw_tolerance_end_2',
                 'ccwset_3', 'ccw_actual_3', 'ccw_error_3', 'ccw_tolerance_start_3', 'ccw_tolerance_end_3',
                  'std_id', 'calibrator', 'certificate_issuer', 'certificate_number', 'status', 'priority']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 Nm'}),
            'cwset': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 Nm', 'step': '0.0001'}),
            'cw0': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'cw90': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'cw180': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'cw270': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'ccwset': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 Nm', 'step': '0.0001'}),
            'ccw0': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'ccw90': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'ccw180': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'ccw270': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'cw_actual': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'cw_error': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'cw_tolerance_start': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 9.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'cw_tolerance_end': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'cwset_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20 Nm', 'step': '0.0001'}),
            'cw_actual_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 Nm', 'step': '0.0001'}),
            'cw_error_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'cw_tolerance_start_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 19.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'cw_tolerance_end_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'cwset_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30 Nm', 'step': '0.0001'}),
            'cw_actual_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 Nm', 'step': '0.0001'}),
            'cw_error_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'cw_tolerance_start_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 29.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'cw_tolerance_end_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccw_actual': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 Nm', 'step': '0.0001'}),
            'ccw_error': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccw_tolerance_start': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 9.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccw_tolerance_end': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccwset_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20 Nm', 'step': '0.0001'}),
            'ccw_actual_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 Nm', 'step': '0.0001'}),
            'ccw_error_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccw_tolerance_start_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 19.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccw_tolerance_end_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccwset_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30 Nm', 'step': '0.0001'}),
            'ccw_actual_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 Nm', 'step': '0.0001'}),
            'ccw_error_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccw_tolerance_start_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 29.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'ccw_tolerance_end_3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.5000 Nm', 'step': '0.0001', 'readonly': 'readonly'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class BalanceCalibrationForm(forms.ModelForm):
    class Meta:
        model = BalanceCalibration
        fields = ['measurement_range', 'date_calibration', 'update', 'next_due', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number', 'status', 'priority',
                  'linear_nominal_value', 'linear_conventional_mass', 'linear_displayed_value', 'linear_error', 'linear_uncertainty',
                  'linear_nominal_value_2', 'linear_conventional_mass_2', 'linear_displayed_value_2', 'linear_error_2', 'linear_uncertainty_2',
                  'linear_nominal_value_3', 'linear_conventional_mass_3', 'linear_displayed_value_3', 'linear_error_3', 'linear_uncertainty_3',
                  'linear_nominal_value_4', 'linear_conventional_mass_4', 'linear_displayed_value_4', 'linear_error_4', 'linear_uncertainty_4',
                  'linear_nominal_value_5', 'linear_conventional_mass_5', 'linear_displayed_value_5', 'linear_error_5', 'linear_uncertainty_5']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 g'}),
            'date_calibration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'linear_nominal_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 g'}),
            'linear_conventional_mass': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 g'}),
            'linear_displayed_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 g'}),
            'linear_error': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 g', 'readonly': 'readonly'}),
            'linear_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0001 g', 'readonly': 'readonly'}),
            'linear_nominal_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 g'}),
            'linear_conventional_mass_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 g'}),
            'linear_displayed_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 g'}),
            'linear_error_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 g', 'readonly': 'readonly'}),
            'linear_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0001 g', 'readonly': 'readonly'}),
            'linear_nominal_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 g'}),
            'linear_conventional_mass_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 g'}),
            'linear_displayed_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 g'}),
            'linear_error_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 g', 'readonly': 'readonly'}),
            'linear_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0001 g', 'readonly': 'readonly'}),
            'linear_nominal_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 g'}),
            'linear_conventional_mass_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 g'}),
            'linear_displayed_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 g'}),
            'linear_error_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 g', 'readonly': 'readonly'}),
            'linear_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0001 g', 'readonly': 'readonly'}),
            'linear_nominal_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 g'}),
            'linear_conventional_mass_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 g'}),
            'linear_displayed_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 g'}),
            'linear_error_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 g', 'readonly': 'readonly'}),
            'linear_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0001 g', 'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class HighFrequencyCalibrationForm(forms.ModelForm):
    class Meta:
        model = HighFrequencyCalibration
        fields = ['measurement_range', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number',
                  'freq_uuc_range', 'freq_uuc_setting', 'freq_measured_value', 'freq_uncertainty', 'freq_tolerance_limit',
                  'freq_uuc_range_2', 'freq_uuc_setting_2', 'freq_measured_value_2', 'freq_uncertainty_2', 'freq_tolerance_limit_2',
                  'freq_uuc_range_3', 'freq_uuc_setting_3', 'freq_measured_value_3', 'freq_uncertainty_3', 'freq_tolerance_limit_3',
                  'freq_uuc_range_4', 'freq_uuc_setting_4', 'freq_measured_value_4', 'freq_uncertainty_4', 'freq_tolerance_limit_4',
                  'freq_uuc_range_5', 'freq_uuc_setting_5', 'freq_measured_value_5', 'freq_uncertainty_5', 'freq_tolerance_limit_5']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 MHz'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            # Frequency Accuracy and Display Calibration - Row 1
            'freq_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 MHz'}),
            'freq_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 MHz'}),
            'freq_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 MHz'}),
            'freq_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'freq_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 2
            'freq_uuc_range_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20 MHz'}),
            'freq_uuc_setting_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 MHz'}),
            'freq_measured_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 MHz'}),
            'freq_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'freq_tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 3
            'freq_uuc_range_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 MHz'}),
            'freq_uuc_setting_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 MHz'}),
            'freq_measured_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 MHz'}),
            'freq_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'freq_tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 4
            'freq_uuc_range_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 MHz'}),
            'freq_uuc_setting_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100.0000 MHz'}),
            'freq_measured_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100.0000 MHz'}),
            'freq_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'freq_tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            # Row 5
            'freq_uuc_range_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 MHz'}),
            'freq_uuc_setting_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200.0000 MHz'}),
            'freq_measured_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200.0000 MHz'}),
            'freq_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'freq_tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class LowFrequencyCalibrationForm(forms.ModelForm):
    class Meta:
        model = LowFrequencyCalibration
        fields = ['measurement_range', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number',
                  # DC VOLTAGE
                  'dc_uuc_range', 'dc_uuc_setting', 'dc_measured_value', 'dc_uncertainty', 'dc_tolerance_limit',
                  'dc_uuc_range_2', 'dc_uuc_setting_2', 'dc_measured_value_2', 'dc_uncertainty_2', 'dc_tolerance_limit_2',
                  'dc_uuc_range_3', 'dc_uuc_setting_3', 'dc_measured_value_3', 'dc_uncertainty_3', 'dc_tolerance_limit_3',
                  'dc_uuc_range_4', 'dc_uuc_setting_4', 'dc_measured_value_4', 'dc_uncertainty_4', 'dc_tolerance_limit_4',
                  'dc_uuc_range_5', 'dc_uuc_setting_5', 'dc_measured_value_5', 'dc_uncertainty_5', 'dc_tolerance_limit_5',
                  # AC VOLTAGE
                  'ac_uuc_range', 'ac_uuc_setting', 'ac_measured_value', 'ac_uncertainty', 'ac_tolerance_limit',
                  'ac_uuc_range_2', 'ac_uuc_setting_2', 'ac_measured_value_2', 'ac_uncertainty_2', 'ac_tolerance_limit_2',
                  'ac_uuc_range_3', 'ac_uuc_setting_3', 'ac_measured_value_3', 'ac_uncertainty_3', 'ac_tolerance_limit_3',
                  'ac_uuc_range_4', 'ac_uuc_setting_4', 'ac_measured_value_4', 'ac_uncertainty_4', 'ac_tolerance_limit_4',
                  'ac_uuc_range_5', 'ac_uuc_setting_5', 'ac_measured_value_5', 'ac_uncertainty_5', 'ac_tolerance_limit_5',
                  # RESISTANCE
                  'res_uuc_range', 'res_uuc_setting', 'res_measured_value', 'res_uncertainty', 'res_tolerance_limit',
                  'res_uuc_range_2', 'res_uuc_setting_2', 'res_measured_value_2', 'res_uncertainty_2', 'res_tolerance_limit_2',
                  'res_uuc_range_3', 'res_uuc_setting_3', 'res_measured_value_3', 'res_uncertainty_3', 'res_tolerance_limit_3',
                  'res_uuc_range_4', 'res_uuc_setting_4', 'res_measured_value_4', 'res_uncertainty_4', 'res_tolerance_limit_4',
                  'res_uuc_range_5', 'res_uuc_setting_5', 'res_measured_value_5', 'res_uncertainty_5', 'res_tolerance_limit_5']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 MHz'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            
            # DC VOLTAGE widgets
            'dc_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_uuc_range_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 mV'}),
            'dc_uuc_setting_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 mV'}),
            'dc_measured_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 mV'}),
            'dc_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_uuc_range_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 mV'}),
            'dc_uuc_setting_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 mV'}),
            'dc_measured_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 mV'}),
            'dc_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_uuc_range_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 mV'}),
            'dc_uuc_setting_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 mV'}),
            'dc_measured_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 mV'}),
            'dc_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_uuc_range_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1000 mV'}),
            'dc_uuc_setting_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1000 mV'}),
            'dc_measured_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1000 mV'}),
            'dc_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            
            # AC VOLTAGE widgets
            'ac_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'ac_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'ac_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'ac_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_uuc_range_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 mV'}),
            'ac_uuc_setting_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 mV'}),
            'ac_measured_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 mV'}),
            'ac_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_uuc_range_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 mV'}),
            'ac_uuc_setting_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 mV'}),
            'ac_measured_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 200 mV'}),
            'ac_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_uuc_range_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 mV'}),
            'ac_uuc_setting_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 mV'}),
            'ac_measured_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 mV'}),
            'ac_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_uuc_range_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1000 mV'}),
            'ac_uuc_setting_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1000 mV'}),
            'ac_measured_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1000 mV'}),
            'ac_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ac_tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            
            # RESISTANCE widgets
            'res_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 Ω'}),
            'res_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 Ω'}),
            'res_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 500 Ω'}),
            'res_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_uuc_range_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 5 kΩ'}),
            'res_uuc_setting_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 5 kΩ'}),
            'res_measured_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 5 kΩ'}),
            'res_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_uuc_range_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 kΩ'}),
            'res_uuc_setting_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 kΩ'}),
            'res_measured_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 kΩ'}),
            'res_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_uuc_range_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 kΩ'}),
            'res_uuc_setting_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 kΩ'}),
            'res_measured_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 kΩ'}),
            'res_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_uuc_range_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 kΩ'}),
            'res_uuc_setting_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 kΩ'}),
            'res_measured_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 100 kΩ'}),
            'res_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'res_tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class MicrowaveCalibrationForm(forms.ModelForm):
    class Meta:
        model = MicrowaveCalibration
        fields = ['next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number',
                  'dc_uuc_range', 'dc_uuc_setting', 'dc_measured_value', 'dc_uncertainty', 'dc_tolerance_limit',
                  'dc_uuc_range_2', 'dc_uuc_setting_2', 'dc_measured_value_2', 'dc_uncertainty_2', 'dc_tolerance_limit_2',
                  'dc_uuc_range_3', 'dc_uuc_setting_3', 'dc_measured_value_3', 'dc_uncertainty_3', 'dc_tolerance_limit_3',
                  'dc_uuc_range_4', 'dc_uuc_setting_4', 'dc_measured_value_4', 'dc_uncertainty_4', 'dc_tolerance_limit_4',
                  'dc_uuc_range_5', 'dc_uuc_setting_5', 'dc_measured_value_5', 'dc_uncertainty_5', 'dc_tolerance_limit_5']
        widgets = {
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'dc_uuc_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_uuc_setting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_measured_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50 mV'}),
            'dc_uncertainty': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_uuc_range_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1.0 GHz'}),
            'dc_uuc_setting_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -10 dBm'}),
            'dc_measured_value_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.9998 GHz'}),
            'dc_uncertainty_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_uuc_range_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 2.0 GHz'}),
            'dc_uuc_setting_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น -5 dBm'}),
            'dc_measured_value_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 1.9998 GHz'}),
            'dc_uncertainty_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_uuc_range_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 5.0 GHz'}),
            'dc_uuc_setting_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0 dBm'}),
            'dc_measured_value_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 4.9998 GHz'}),
            'dc_uncertainty_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_uuc_range_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0 GHz'}),
            'dc_uuc_setting_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น +5 dBm'}),
            'dc_measured_value_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 9.9998 GHz'}),
            'dc_uncertainty_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'dc_tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class DialGaugeCalibrationForm(forms.ModelForm):
    class Meta:
        model = DialGaugeCalibration
        fields = ['measurement_range', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer',
                  'uuc_set', 'actual', 'error', 'uncertainty', 'tolerance_limit',
                  'set_2', 'actual_2', 'error_2', 'tolerance_limit_2',
                  'set_3', 'actual_3', 'error_3', 'tolerance_limit_3',
                  'set_4', 'actual_4', 'error_4', 'tolerance_limit_4',
                  'set_5', 'actual_5', 'error_5', 'tolerance_limit_5']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 mm'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
            'calibrator': forms.Select(attrs={'class': 'form-control'}),
            'certificate_issuer': forms.Select(attrs={'class': 'form-control'}),
            'uuc_set': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 inch'}),
            'actual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 inch'}),
            'error': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 inch', 'readonly': 'readonly'}),
            'uncertainty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0001 inch', 'readonly': 'readonly'}),
            'tolerance_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 9.9990 – 10.0010 inch', 'readonly': 'readonly'}),
            'set_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 inch'}),
            'actual_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 20.0000 inch'}),
            'error_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 inch', 'readonly': 'readonly'}),
            'tolerance_limit_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 19.9990 – 20.0010 inch', 'readonly': 'readonly'}),
            'set_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 inch'}),
            'actual_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 30.0000 inch'}),
            'error_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 inch', 'readonly': 'readonly'}),
            'tolerance_limit_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 29.9990 – 30.0010 inch', 'readonly': 'readonly'}),
            'set_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 inch'}),
            'actual_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 40.0000 inch'}),
            'error_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 inch', 'readonly': 'readonly'}),
            'tolerance_limit_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 39.9990 – 40.0010 inch', 'readonly': 'readonly'}),
            'set_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 inch'}),
            'actual_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 50.0000 inch'}),
            'error_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0.0000 inch', 'readonly': 'readonly'}),
            'tolerance_limit_5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 49.9990 – 50.0010 inch', 'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า queryset สำหรับฟิลด์ calibrator และ certificate_issuer
        User = get_user_model()
        users = User.objects.filter(is_active=True).order_by('first_name', 'last_name', 'username')
        self.fields['calibrator'].queryset = users
        self.fields['certificate_issuer'].queryset = users
        
        # ตั้งค่า queryset สำหรับเครื่องมือที่ใช้สอบเทียบ
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.all().order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"
