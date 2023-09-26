from rest_framework import serializers

from course.models import Course, Lesson, Payments, Subscription
from course.services import creates_payment_intent, retrieve_payment_intent
from course.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    validators = [UrlValidator(field='url')]
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(many=True, read_only=True)
    validators = [UrlValidator(field='url')]
    subscription = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    def get_lesson_count(self, instance):
        return instance.lesson.all().count()

    def get_subscription(self, instance):
        user = self.request.user
        sub_all = instance.subscription.all()
        for sub in sub_all:
            if sub.subscriber == user:
                return True
        # if not instance.subscription.all():
        #     return False
        return False

    class Meta:
        model = Course
        fields = ['pk', 'name', 'image', 'description', 'owner', 'subscription', 'lesson', 'lesson_count']


class PaymentsSerializer(serializers.ModelSerializer):
    payment_stripe = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    def get_payment_stripe(self, instance):
        if self.request.stream.method == 'POST':
            payment_stripe_id = creates_payment_intent(int(instance.sum_pay))
            obj_payments = Payments.objects.get(id=instance.id)
            obj_payments.payment_stripe_id = payment_stripe_id
            obj_payments.save()
            return retrieve_payment_intent(payment_stripe_id)
        if self.request.stream.method == 'GET':
            if not instance.payment_stripe_id:
                return None
            return retrieve_payment_intent(instance.payment_stripe_id)

    class Meta:
        model = Payments
        fields = ['user', 'date_pay', 'type_metod', 'sum_pay', 'payment_method', 'payment_stripe']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
