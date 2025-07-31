from django import forms
from .models import TechnicalDocument

class TechnicalDocumentForm(forms.ModelForm):
    class Meta:
        model = TechnicalDocument
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อเอกสาร'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'คำอธิบายเอกสาร'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'ชื่อเอกสาร',
            'description': 'คำอธิบาย',
            'file': 'ไฟล์เอกสาร',
        } 