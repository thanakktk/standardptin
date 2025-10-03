import re

# อ่านไฟล์
with open('calibrate/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# แก้ไข indentation error
content = re.sub(
    r'^([ \t]+)(\'calibration_date\': cal\.update,\s*#[^\n]+)$',
    r'    #         \2',
    content,
    flags=re.MULTILINE
)

# เขียนไฟล์
with open('calibrate/views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed indentation error!")

