from django import forms
from django.contrib.auth import get_user_model
from .models import (
    CalibrationPressure, CalibrationTorque, BalanceCalibration, 
    HighFrequencyCalibration, LowFrequencyCalibration, MicrowaveCalibration, DialGaugeCalibration
)

class CalibrationPressureForm(forms.ModelForm):
    class Meta:
        model = CalibrationPressure
        fields = ['measurement_range', 'set', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 bar'}),
            'set': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10 bar'}),
            'm1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm6': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm7': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm8': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm9': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
            'm10': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 10.0000 bar'}),
        }

class CalibrationTorqueForm(forms.ModelForm):
    class Meta:
        model = CalibrationTorque
        fields = ['measurement_range', 'cwset', 'cw0', 'cw90', 'cw180', 'cw270', 'ccwset', 'ccw0', 'ccw90', 'ccw180', 'ccw270']
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
        }

class BalanceCalibrationForm(forms.ModelForm):
    class Meta:
        model = BalanceCalibration
        fields = ['measurement_range', 'date_calibration', 'update', 'next_due', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number', 'status', 'priority']
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
        self.fields['std_id'].queryset = CalibrationEquipment.objects.filter(is_active=True).order_by('name')
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
        self.fields['std_id'].queryset = CalibrationEquipment.objects.filter(is_active=True).order_by('name')
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
        self.fields['std_id'].queryset = CalibrationEquipment.objects.filter(is_active=True).order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class MicrowaveCalibrationForm(forms.ModelForm):
    class Meta:
        model = MicrowaveCalibration
        fields = ['measurement_range', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 GHz'}),
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
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.filter(is_active=True).order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"

class DialGaugeCalibrationForm(forms.ModelForm):
    class Meta:
        model = DialGaugeCalibration
        fields = ['measurement_range', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number']
        widgets = {
            'measurement_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 0-100 mm'}),
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
        from machine.models import CalibrationEquipment
        self.fields['std_id'].queryset = CalibrationEquipment.objects.filter(is_active=True).order_by('name')
        self.fields['std_id'].empty_label = "เลือกเครื่องมือที่ใช้สอบเทียบ"
