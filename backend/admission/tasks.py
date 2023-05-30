from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from admission.models import Admission

@shared_task
def send_admission_emails():
    admissions = Admission.objects.filter(status=False)
    for admission in admissions:
        admission.send_email()
