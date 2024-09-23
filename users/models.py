from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    city = models.CharField(
        max_length=35,
        verbose_name="Город",
        blank=True,
        null=True,
        help_text="Укажите город",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_CASH = 'cash'
    PAYMENT_TRANSFER = 'transfer'
    PAYMENT_CHOICES = (
        (PAYMENT_CASH, 'Оплата наличными'),
        (PAYMENT_TRANSFER, 'Безналичная оплата'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Оплаченный курс',
        blank=True,
        null=True
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='Оплаченный урок',
        blank=True,
        null=True
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    payment_type = models.CharField(
        max_length=50,
        choices=PAYMENT_CHOICES,
        verbose_name="Способ оплаты"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["-date"]

    def __str__(self):
        return f'{self.user.email} - {self.paid_lesson.title if self.paid_lesson else self.paid_course.title}'
    