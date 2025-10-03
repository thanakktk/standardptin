from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from functools import wraps


def permission_required(permission):
    """
    Decorator สำหรับตรวจสอบสิทธิ์การใช้งาน
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            
            if not request.user.can_access_feature(permission):
                raise PermissionDenied("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def unit_user_required(view_func):
    """
    Decorator สำหรับตรวจสอบว่าเป็นผู้ใช้หน่วยงาน
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if not request.user.is_unit_user():
            raise PermissionDenied("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
        
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    """
    Decorator สำหรับตรวจสอบว่าเป็นผู้ดูแลระบบ
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if not request.user.is_admin_user():
            raise PermissionDenied("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
        
        return view_func(request, *args, **kwargs)
    return wrapper


def technician_required(view_func):
    """
    Decorator สำหรับตรวจสอบว่าเป็นช่างเทคนิค
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if not request.user.is_technician():
            raise PermissionDenied("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
        
        return view_func(request, *args, **kwargs)
    return wrapper


class PermissionRequiredMixin:
    """
    Mixin สำหรับตรวจสอบสิทธิ์ใน Class-based views
    """
    permission_required = None
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        
        if self.permission_required and not request.user.can_access_feature(self.permission_required):
            raise PermissionDenied("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
        
        return super().dispatch(request, *args, **kwargs)


class UnitUserRequiredMixin:
    """
    Mixin สำหรับตรวจสอบว่าเป็นผู้ใช้หน่วยงาน
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if not request.user.is_unit_user():
            raise PermissionDenied("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
        
        return super().dispatch(request, *args, **kwargs)


class AdminRequiredMixin:
    """
    Mixin สำหรับตรวจสอบว่าเป็นผู้ดูแลระบบ
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if not request.user.is_admin_user():
            raise PermissionDenied("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
        
        return super().dispatch(request, *args, **kwargs)


class TechnicianRequiredMixin:
    """
    Mixin สำหรับตรวจสอบว่าเป็นช่างเทคนิค
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        if not request.user.is_technician():
            raise PermissionDenied("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
        
        return super().dispatch(request, *args, **kwargs)
