# core/email_backends.py
import socket
from smtplib import SMTP, SMTP_SSL
from django.core.mail.backends.smtp import EmailBackend

class IPv4EmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False

        # เลือก class ตามโหมด
        connection_class = SMTP_SSL if self.use_ssl else SMTP

        # บังคับ resolve แบบ IPv4 เท่านั้น
        infos = socket.getaddrinfo(self.host, self.port, socket.AF_INET, socket.SOCK_STREAM)
        af, socktype, proto, canonname, sa = infos[0]

        # เปิด connection เอง แล้วค่อย starttls/login ตามปกติ
        self.connection = connection_class(timeout=self.timeout)
        self.connection.connect(sa[0], sa[1])
        if not self.use_ssl and self.use_tls:
            self.connection.starttls(context=self.ssl_context)
        if self.username and self.password:
            self.connection.login(self.username, self.password)
        return True
