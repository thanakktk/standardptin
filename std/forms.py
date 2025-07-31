from django import forms
from .models import Standard

class StandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = '__all__' 