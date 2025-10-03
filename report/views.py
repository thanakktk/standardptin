from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.permissions import permission_required

@login_required
@permission_required('view_reports')
def report_list(request):
    """แสดงหน้ารายงาน"""
    return render(request, 'report/list.html')

@login_required
@permission_required('export_reports')
def export_word(request):
    """ส่งออกรายงานเป็น Word"""
    # Logic for Word export
    return render(request, 'report/export_word.html')

@login_required
@permission_required('export_reports')
def export_excel(request):
    """ส่งออกรายงานเป็น Excel"""
    # Logic for Excel export
    return render(request, 'report/export_excel.html')

@login_required
@permission_required('download_certificates')
def download_certificate(request):
    """ดาวน์โหลดใบรับรอง"""
    # Logic for certificate download
    return render(request, 'report/download_certificate.html')
