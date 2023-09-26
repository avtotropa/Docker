from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course.models import Course, Subscription


@shared_task
def send_course_update(course_id):
    course = Course.objects.get(pk=course_id)
    sub_couse = Subscription.objects.filter(course=course_id)
    for sub in sub_couse:
        send_mail(subject=f"{course.name}",
                  message=f"{course.name}",
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[f'{sub.subscriber}'],
                  fail_silently=True
                  )
