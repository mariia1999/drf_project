# Generated by Django 5.1.1 on 2024-09-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={
                "ordering": ["-date"],
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_type",
            field=models.BooleanField(
                default=True,
                verbose_name="Тип оплаты (безнал - True, наличные - False)",
            ),
        ),
    ]
