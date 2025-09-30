"""
Shared Mixins for Calibration Views
"""
from __future__ import annotations

from django.http import QueryDict


class ActiveUsersMixin:
    """Populate calibrator/certificate_issuer with active users."""
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            users = (
                User.objects.filter(is_active=True)
                .order_by("first_name", "last_name", "username")
            )
            if "calibrator" in form.fields:
                form.fields["calibrator"].queryset = users
            if "certificate_issuer" in form.fields:
                form.fields["certificate_issuer"].queryset = users
        except Exception:
            pass
        return form


class StatusDefaultMixin:
    """Ensure a default status is injected on POST if missing."""
    
    default_status = "in_progress"
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST" and "status" not in self.request.POST:
            data = kwargs.get("data")
            if data is None:
                data = QueryDict(mutable=True)
            else:
                data = data.copy()
            # Keep current object status if present (Update), else default
            current = getattr(getattr(self, "object", None), "status", None)
            data["status"] = current or self.default_status
            kwargs["data"] = data
        return kwargs
