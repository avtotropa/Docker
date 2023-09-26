from django.db import models

from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='course/', verbose_name='Изображение', **NULLABLE)
    url = models.URLField(verbose_name='Cсылка на видео', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name='subscription', verbose_name='Подписка на курс')
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Подписчик', **NULLABLE)

    def __str__(self):
        return f'{self.course}:{self.subscriber}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name='lesson')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='lesson/', verbose_name='Изображение', **NULLABLE)
    url = models.URLField(verbose_name='Cсылка на видео', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE,verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', verbose_name='пользователь')
    date_pay = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    type_metod = models.CharField(choices=(('Course', 'Курс'), ('Lesson', 'Урок')), verbose_name='оплаченный курс или урок')
    sum_pay = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(choices=(('Cash', 'Наличные '), ('Account_transfer', 'Перевод на счет')), verbose_name='наличные или перевод на счет')
    payment_stripe_id = models.CharField(max_length=255,verbose_name='id платежа на stripe', **NULLABLE)

    def __str__(self):
        return f'{self.user}:{self.date_pay} на сумму{self.sum_pay}'

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
