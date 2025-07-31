from django import forms
from .models import Organize

class OrganizeForm(forms.ModelForm):
    class Meta:
        model = Organize
        fields = ['name', 'parent', 'is_main_unit', 'address', 'phone', 'email', 'users']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'is_main_unit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'users': forms.SelectMultiple(attrs={'class': 'form-control'}),
        } 