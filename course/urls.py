from django.urls import path
from rest_framework import routers

from course.apps import CourseConfig
from course.serializers import LessonSerializer
from course.views import LessonListAPIView, LessonDetailAPIView, LessonCreateAPIView, LessonDestroyAPIView, \
    LessonUpdateAPIView, CourseViewSet, PaymentsViewSet, SubscriptionViewSet

app_name = CourseConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'payments', PaymentsViewSet)
router.register(r'subscription', SubscriptionViewSet)

urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
                  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
              ] + router.urls
