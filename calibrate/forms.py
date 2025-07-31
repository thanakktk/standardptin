from django import forms
from .models import CalibrationForce, CalibrationPressure, CalibrationTorque

class CalibrationForceForm(forms.ModelForm):
    class Meta:
        model = CalibrationForce
        fields = ['apply_com', 'apply_ten', 'compress', 'tension', 'fullscale', 'error', 'tolerance_start', 'tolerance_end', 'update', 'next_due', 'status', 'priority', 'uuc_id', 'std_id']
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
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'uuc_id': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
        }

class CalibrationPressureForm(forms.ModelForm):
    class Meta:
        model = CalibrationPressure
        fields = ['set', 'm1', 'm2', 'm3', 'm4', 'avg', 'error', 'tolerance_start', 'tolerance_end', 'update', 'next_due', 'status', 'priority', 'uuc_id', 'std_id']
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
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'uuc_id': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
        }

class CalibrationTorqueForm(forms.ModelForm):
    class Meta:
        model = CalibrationTorque
        fields = ['cwset', 'cw0', 'cw90', 'cw180', 'cw270', 'cw_reading', 'cw_avg', 'cw_error', 'cw_tolerance_start', 'cw_tolerance_end', 'ccwset', 'ccw0', 'ccw90', 'ccw180', 'ccw270', 'ccw_reading', 'ccw_avg', 'ccw_error', 'ccw_tolerance_start', 'ccw_tolerance_end', 'update', 'next_due', 'status', 'priority', 'uuc_id', 'std_id']
        widgets = {
            'cwset': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw0': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw90': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw180': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw270': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_reading': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_avg': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cw_error': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_tolerance_start': forms.NumberInput(attrs={'class': 'form-control'}),
            'cw_tolerance_end': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccwset': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw0': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw90': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw180': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw270': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_reading': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_avg': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ccw_error': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_tolerance_start': forms.NumberInput(attrs={'class': 'form-control'}),
            'ccw_tolerance_end': forms.NumberInput(attrs={'class': 'form-control'}),
            'update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'uuc_id': forms.Select(attrs={'class': 'form-control'}),
            'std_id': forms.Select(attrs={'class': 'form-control'}),
        } 