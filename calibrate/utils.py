"""
Utility functions for calibration system
"""
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


def calculate_next_due_date(calibration_date):
    """
    คำนวณวันที่ครบกำหนดสอบเทียบครั้งถัดไป (เพิ่ม 6 เดือนจากวันที่สอบเทียบ)
    
    Args:
        calibration_date: วันที่สอบเทียบ (date object หรือ string)
    
    Returns:
        date: วันที่ครบกำหนดสอบเทียบครั้งถัดไป
    """
    if not calibration_date:
        return None
    
    # แปลง string เป็น date object ถ้าจำเป็น
    if isinstance(calibration_date, str):
        try:
            calibration_date = datetime.strptime(calibration_date, '%Y-%m-%d').date()
        except ValueError:
            try:
                calibration_date = datetime.strptime(calibration_date, '%d/%m/%Y').date()
            except ValueError:
                return None
    
    # คำนวณ 6 เดือนจากวันที่สอบเทียบ
    try:
        next_due = calibration_date + relativedelta(months=6)
        return next_due
    except Exception:
        # Fallback method using manual calculation
        year = calibration_date.year
        month = calibration_date.month + 6
        if month > 12:
            year += month // 12
            month = month % 12
            if month == 0:
                month = 12
        
        # ใช้วันที่เดิม แต่เปลี่ยนปีและเดือน
        day = min(calibration_date.day, 28)  # ป้องกันปัญหาเดือนกุมภาพันธ์
        try:
            return datetime(year, month, day).date()
        except ValueError:
            # ถ้าวันที่ไม่ถูกต้อง ให้ใช้วันที่ 28 ของเดือนนั้น
            return datetime(year, month, 28).date()


def calculate_next_due_from_update_date(update_date):
    """
    คำนวณวันที่ครบกำหนดสอบเทียบครั้งถัดไปจากวันที่อัปเดต
    
    Args:
        update_date: วันที่อัปเดต (date object หรือ string)
    
    Returns:
        date: วันที่ครบกำหนดสอบเทียบครั้งถัดไป
    """
    return calculate_next_due_date(update_date)
