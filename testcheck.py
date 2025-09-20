from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException, SMTPServerDisconnected
from django.http import HttpResponse

def send_machine_email(request, pk):
    try:
        sent = send_mail(
            subject='Test Email',
            message='Hello from Django!',
            from_email=None,
            recipient_list=['pakka.sort@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse(f"OK sent={sent}")
    except (SMTPServerDisconnected, SMTPException, BadHeaderError) as e:
        return HttpResponse(f"SMTP error: {type(e).__name__}: {e}", status=500)
    except Exception as e:
        return HttpResponse(f"Other error: {type(e).__name__}: {e}", status=500)
