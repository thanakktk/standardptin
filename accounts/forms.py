from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    # ข้อมูลพื้นฐาน
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อผู้ใช้'}),
        label="ชื่อผู้ใช้"
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
        label="อีเมล"
    )
    
    # คำนำหน้า
    prefix = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'นาย/นาง/นางสาว'}),
        label="คำนำหน้า"
    )
    
    # ชื่อภาษาไทย
    first_name_th = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อภาษาไทย'}),
        label="ชื่อ (ไทย)"
    )
    last_name_th = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'นามสกุลภาษาไทย'}),
        label="นามสกุล (ไทย)"
    )
    
    # ชื่อภาษาอังกฤษ
    first_name_en = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        label="ชื่อ (อังกฤษ)"
    )
    last_name_en = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        label="นามสกุล (อังกฤษ)"
    )
    
    # เบอร์โทรศัพท์
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '081-234-5678'}),
        label="เบอร์โทรศัพท์"
    )
    phone_extension = forms.CharField(
        max_length=5,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345'}),
        label="เบอร์โทรศัพท์ 5 หลัก"
    )
    
    # หน่วยงาน
    organize = forms.ModelChoiceField(
        queryset=User._meta.get_field('organize').related_model.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="หน่วยงาน"
    )
    
    # รหัสผ่าน
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'รหัสผ่าน'}),
        label="รหัสผ่าน"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'ยืนยันรหัสผ่าน'}),
        label="ยืนยันรหัสผ่าน"
    )

    class Meta:
        model = User
        fields = (
            "username", "email", "prefix",
            "first_name_th", "last_name_th",
            "first_name_en", "last_name_en",
            "phone", "phone_extension", "organize",
            "password1", "password2"
        )

    def clean_phone_extension(self):
        """ตรวจสอบเบอร์โทรศัพท์ 5 หลัก"""
        phone_extension = self.cleaned_data.get('phone_extension')
        if phone_extension:
            if not phone_extension.isdigit() or len(phone_extension) != 5:
                raise forms.ValidationError("เบอร์โทรศัพท์ 5 หลักต้องเป็นตัวเลข 5 หลัก")
        return phone_extension

    def clean(self):
        """ตรวจสอบข้อมูลเพิ่มเติม"""
        cleaned_data = super().clean()
        first_name_th = cleaned_data.get('first_name_th')
        last_name_th = cleaned_data.get('last_name_th')
        first_name_en = cleaned_data.get('first_name_en')
        last_name_en = cleaned_data.get('last_name_en')
        
        # ตรวจสอบว่าต้องมีชื่ออย่างน้อยภาษาใดภาษาหนึ่ง
        if not (first_name_th and last_name_th) and not (first_name_en and last_name_en):
            raise forms.ValidationError("กรุณากรอกชื่อและนามสกุลอย่างน้อยภาษาใดภาษาหนึ่ง")
        
        return cleaned_data 