from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
import os
import urllib.parse
from .models import TechnicalDocument
from .forms import TechnicalDocumentForm

@login_required
def document_list(request):
    """แสดงรายการเอกสารเทคนิคทั้งหมด"""
    documents = TechnicalDocument.objects.all()
    return render(request, 'technical_docs/document_list.html', {
        'documents': documents
    })

@login_required
def upload_document(request):
    """อัพโหลดเอกสารใหม่"""
    if request.method == 'POST':
        form = TechnicalDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'อัพโหลดเอกสารสำเร็จ')
            return redirect('technical_docs:document_list')
        else:
            messages.error(request, 'เกิดข้อผิดพลาดในการอัพโหลด')
    else:
        form = TechnicalDocumentForm()
    
    return render(request, 'technical_docs/upload_form.html', {
        'form': form
    })

@login_required
def download_document(request, pk):
    """ดาวน์โหลดเอกสาร"""
    import urllib.parse
    document = get_object_or_404(TechnicalDocument, pk=pk)
    file_path = document.file.path
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/octet-stream')
            filename = document.original_filename or document.filename()
            try:
                encoded_filename = urllib.parse.quote(filename)
                response['Content-Disposition'] = f"attachment; filename*=UTF-8''{encoded_filename}"
            except Exception:
                # fallback เป็นชื่อไฟล์อังกฤษง่ายๆ
                import re
                safe_filename = re.sub(r'[^\w\s-]', '_', filename)
                safe_filename = re.sub(r'[-\s]+', '_', safe_filename)
                safe_filename = safe_filename.strip('_')
                # ตรวจสอบนามสกุลไฟล์
                if '.' in filename:
                    file_extension = filename.split('.')[-1]
                    safe_filename = f"{safe_filename}.{file_extension}"
                response['Content-Disposition'] = f'attachment; filename="{safe_filename}"'
            return response
    else:
        messages.error(request, 'ไม่พบไฟล์')
        return redirect('technical_docs:document_list')

@login_required
def delete_document(request, pk):
    """ลบเอกสาร"""
    document = get_object_or_404(TechnicalDocument, pk=pk)
    if request.method == 'POST':
        document.delete()
        messages.success(request, 'ลบเอกสารสำเร็จ')
        return redirect('technical_docs:document_list')
    
    return render(request, 'technical_docs/confirm_delete.html', {
        'document': document
    })
