def user_permissions(request):
    """
    Context processor เพื่อให้สิทธิ์ผู้ใช้สามารถใช้ใน template ได้
    """
    if request.user.is_authenticated:
        return {
            'user_permissions': {
                'can_view_machine': request.user.can_access_feature('view_machine'),
                'can_add_machine': request.user.can_access_feature('add_machine'),
                'can_edit_machine': request.user.can_access_feature('edit_machine'),
                'can_delete_machine': request.user.can_access_feature('delete_machine'),
                'can_send_notification': request.user.can_access_feature('send_notification'),
                'can_view_calibration': request.user.can_access_feature('view_calibration'),
                'can_add_calibration': request.user.can_access_feature('add_calibration'),
                'can_edit_calibration': request.user.can_access_feature('edit_calibration'),
                'can_delete_calibration': request.user.can_access_feature('delete_calibration'),
                'can_view_organization': request.user.can_access_feature('view_organization'),
                'can_manage_organization': request.user.can_access_feature('manage_organization'),
                'can_view_users': request.user.can_access_feature('view_users'),
                'can_manage_users': request.user.can_access_feature('manage_users'),
                'can_view_equipment': request.user.can_access_feature('view_equipment'),
                'can_manage_equipment': request.user.can_access_feature('manage_equipment'),
                'can_view_technical_docs': request.user.can_access_feature('view_technical_docs'),
                'can_manage_technical_docs': request.user.can_access_feature('manage_technical_docs'),
                'can_view_reports': request.user.can_access_feature('view_reports'),
                'can_export_reports': request.user.can_access_feature('export_reports'),
                'can_edit_reports': request.user.can_access_feature('edit_reports'),
                'can_download_certificates': request.user.can_access_feature('download_certificates'),
                'can_change_priority': request.user.can_access_feature('change_priority'),
                'can_close_work': request.user.can_access_feature('close_work'),
                'can_access_admin': request.user.can_access_feature('access_admin'),
            },
            'is_unit_user': request.user.is_unit_user(),
            'is_admin_user': request.user.is_admin_user(),
            'is_technician': request.user.is_technician(),
            'is_coordinator': request.user.is_coordinator(),
        }
    return {
        'user_permissions': {},
        'is_unit_user': False,
        'is_admin_user': False,
        'is_technician': False,
        'is_coordinator': False,
    }
