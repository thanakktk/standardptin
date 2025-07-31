import smtplib

try:
    with smtplib.SMTP('smtp.gmail.com', 587, timeout=15) as server:
        server.starttls()
        server.login('pakka.sort@gmail.com', 'youcfprnjwwugiuc')
        server.sendmail(
            'pakka.sort@gmail.com',
            'someone@example.com',
            'Subject: Hello\n\nThis is a test email.'
        )
except Exception as e:
    print("❌ ERROR:", e)
