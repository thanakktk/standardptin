from django import forms
from django.contrib.auth import get_user_model
from organize.models import Organize

User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'prefix', 'first_name_th', 'last_name_th', 
            'first_name_en', 'last_name_en', 'phone', 'phone_extension', 
            'organize', 'level', 'is_active', 'is_staff'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'prefix': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name_th': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name_th': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name_en': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name_en': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_extension': forms.TextInput(attrs={'class': 'form-control'}),
            'organize': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organize'].queryset = Organize.objects.all()
        self.fields['organize'].empty_label = "เลือกหน่วยงาน" 