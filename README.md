# Projest (Django Version)

ระบบปรับเทียบเครื่องวัด (Calibration Management System) เวอร์ชัน Python + Django

## วิธีเริ่มต้น

1. สร้าง virtualenv และติดตั้ง dependencies

```bash
python -m venv venv
venv\Scripts\activate  # หรือ source venv/bin/activate (บน macOS/Linux)
pip install -r requirements.txt
```

2. สร้างฐานข้อมูลและ migrate

```bash
python manage.py migrate
```

3. สร้าง superuser (admin)

```bash
python manage.py createsuperuser
```

4. รันเซิร์ฟเวอร์

```bash
python manage.py runserver
```

## โครงสร้างโปรเจ็ค
- projest/ (Django project settings)
- accounts/ (ระบบผู้ใช้/ยืนยันตัวตน)
- machine/ (เครื่องวัด)
- calibrate/ (บันทึกการปรับเทียบ)
- cert/ (ใบรับรอง)
- report/ (รายงาน)
- employee/ (พนักงาน)
- organize/ (หน่วยงาน/องค์กร) 