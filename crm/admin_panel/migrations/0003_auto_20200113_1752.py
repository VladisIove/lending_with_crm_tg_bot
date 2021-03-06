# Generated by Django 3.0.2 on 2020-01-13 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_auto_20200113_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='type_order',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Быстрый заказ'), (2, 'Полный заказ')], default=1),
        ),
        migrations.AlterField(
            model_name='clothesview',
            name='img',
            field=models.ImageField(upload_to='media/', verbose_name='Фотография профиля'),
        ),
        migrations.AlterField(
            model_name='clothesview',
            name='old_price',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
