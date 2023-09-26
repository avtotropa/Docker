from django.core.management import BaseCommand

from course.models import Payments
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        Pay_1 = Payments.objects.create(
            user=User.objects.get(email='admin@1jz.ru'),
            type_metod='Course',
            sum_pay=10561.25,
            payment_method='Cash'

        )
        Pay_1.save()
        Pay_2 = Payments.objects.create(
            user=User.objects.get(email='test@1jz.ru'),
            type_metod='Lesson',
            sum_pay=1519.95,
            payment_method='Account_transfer'

        )
        Pay_2.save()

