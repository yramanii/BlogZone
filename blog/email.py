from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_email(First_Name, Email, Description):

    context = {
        'First_Name': First_Name,
        'Email': Email,
        'Description': Description,
    }

    email_subject = 'Thank you for your review'
    email_body = render_to_string('email_text.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [Email, ],
    )
    return email.send(fail_silently=False)