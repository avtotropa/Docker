from django.contrib import admin

from course.models import Course, Lesson, Subscription, Payments

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Subscription)
admin.site.register(Payments)
