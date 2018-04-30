from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email_update_notification(email):
    msg_body = render_to_string(
        'allauth/account/email/email_changed_notification.txt')
    send_mail(
        ("Change of email at Acumen"),
        msg_body,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
