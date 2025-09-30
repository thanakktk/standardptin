#!/usr/bin/env python3
import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projest.settings')
django.setup()

from django.conf import settings
from docx import Document
from docx.oxml.ns import qn

TEMPLATE = os.path.join(settings.BASE_DIR, "Low Frequency_template.docx")
OUTPUT   = os.path.join(settings.BASE_DIR, "test_low_frequency_output.docx")

# --- replacer: รวมทุก run ในย่อหน้าแล้วแทนทีเดียว (กันโดน split runs) ---
def replace_in_paragraph_strict(paragraph, repl: dict):
    runs = paragraph.runs
    if not runs: return
    full = "".join(r.text for r in runs)
    new  = full
    for k, v in repl.items():
        if k in new:
            new = new.replace(k, str(v))
    if new == full: return
    for i in range(len(runs)-1, -1, -1):
        r = runs[i]
        r._element.getparent().remove(r._element)
    paragraph.add_run(new)

def replace_in_doc(doc, repl: dict):
    for p in doc.paragraphs:
        replace_in_paragraph_strict(p, repl)
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    replace_in_paragraph_strict(p, repl)

# --- XPath ครอบคลุม w:t ทั้งไฟล์ (ดึงข้อความที่ python-docx ไม่ expose เช่นใน text box/shape) ---
NSMAP = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def _replace_all_text_nodes(part, repl: dict):
    """
    แทนค่าทุก w:t ภายใน part (รองรับ text box/shape, header/footer)
    โดยไม่ใช้ namespaces= ซึ่ง python-docx รุ่นนี้ไม่รองรับ
    """
    if not hasattr(part, "element"):
        return
    w_t = qn('w:t')  # -> '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'
    for t in part.element.iter(w_t):
        txt = t.text or ""
        new = txt
        for k, v in repl.items():
            if k in new:
                new = new.replace(k, str(v))
        if new != txt:
            t.text = new

def replace_everywhere(doc, repl: dict):
    _replace_all_text_nodes(doc, repl)                 # main document
    for sec in doc.sections:                           # headers/footers
        if getattr(sec, "header", None):
            _replace_all_text_nodes(sec.header.part, repl)
        if getattr(sec, "footer", None):
            _replace_all_text_nodes(sec.footer.part, repl)

# --- helper ระบุ placeholder ที่ยังเหลือ (debug) ---
def find_left_placeholders(doc):
    leftovers = []
    def grab(txt):
        if "{{" in txt and "}}" in txt:
            leftovers.append(txt)
    for p in doc.paragraphs: grab(p.text)
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                grab(cell.text)
    return leftovers

def main():
    if not os.path.exists(TEMPLATE):
        print("❌ ไม่พบ template:", TEMPLATE); return
    doc = Document(TEMPLATE)

    # ✅ ใช้ “dict เดียว” รวมทุก placeholder (หัวเอกสาร + DC/AC/RES)
    ctx = {
        # header/common
        "{{MODEL}}": "Test Model",
        "{{MANUFACTURER}}": "Test Manufacturer",
        "{{DESCRIPTION}}": "Test Description",
        "{{SERIAL_NUMBER}}": "TEST123",
        "{{RANGE}}": "0-100 Hz",
        "{{GRADUATION}}": "0.1 Hz",
        "{{CUSTOMER_ASSET_ID}}": "ASSET001",
        "{{RECEIVED_DATE}}": "01-Jan-2025",
        "{{DATE_OF_CALIBRATION}}": "02-Jan-2025",
        "{{DUE_DATE}}": "02-Jan-2026",
        "{{ISSUE_DATE}}": "03-Jan-2025",
        "{{CERTIFICATE_NUMBER}}": "CERT001",
        "{{PROCEDURE}}": "PROC001",
        "{{STANDARD_ASSET_NO}}": "STD001",
        "{{STANDARD_DESCRIPTION}}": "Standard Description",
        "{{STANDARD_MAKER_MODEL}}": "Standard Model",
        "{{STANDARD_SERIAL}}": "STD123",
        "{{STANDARD_CERTIFICATE}}": "STDCERT001",
        "{{STANDARD_DUE_DATE}}": "01-Jan-2026",
        "{{CALIBRATOR}}": "Test Calibrator",
        "{{APPROVER}}": "Test Approver",
        "{{CUSTOMER}}": "Test Customer",
        "{{CUSTOMER_ADDRESS}}": "Test Address",
        "{{LOCATION_OF_CALIBRATION}}": "Test Location",
        "{{LOCATION_ADDRESS}}": "Test Location Address",

        # DC/AC/RES row 1 (ทดสอบตัวอย่าง)
        "{{DC_UUC_RANGE_1}}": "50 mV",
        "{{DC_UUC_SETTING_1}}": "50 mV",
        "{{DC_MEASURED_VALUE_1}}": "50 mV",
        "{{DC_UNCERTAINTY_1}}": "0.0000 mV",
        "{{DC_TOLERANCE_LIMIT_1}}": "49.0035 – 50.0065 mV",

        "{{AC_UUC_RANGE_1}}": "50 mV",
        "{{AC_UUC_SETTING_1}}": "50 mV",
        "{{AC_MEASURED_VALUE_1}}": "50 mV",
        "{{AC_UNCERTAINTY_1}}": "0.0000 mV",
        "{{AC_TOLERANCE_LIMIT_1}}": "45.0080 – 50.0020 mV",

        "{{RES_UUC_RANGE_1}}": "500 Ω",
        "{{RES_UUC_SETTING_1}}": "500 Ω",
        "{{RES_MEASURED_VALUE_1}}": "500 Ω",
        "{{RES_UNCERTAINTY_1}}": "0.0000 Ω",
        "{{RES_TOLERANCE_LIMIT_1}}": "499.0077 – 50.0033 Ω",
    }

    # แทนค่าทั้งแบบ strict (paragraph/table) และแบบ XPath (เผื่อ text box/shape)
    replace_in_doc(doc, ctx)
    replace_everywhere(doc, ctx)

    # รายงาน placeholder ที่ยังเหลือ (ถ้ามี)
    leftovers = find_left_placeholders(doc)
    if leftovers:
        print("⚠️ placeholder ยังเหลืออยู่ (ตรวจสะกดชื่อในไฟล์ .docx):")
        for s in leftovers[:10]:
            print("   •", s.strip()[:120])

    doc.save(OUTPUT)
    print("✅ บันทึกไฟล์:", OUTPUT)

if __name__ == "__main__":
    main()
