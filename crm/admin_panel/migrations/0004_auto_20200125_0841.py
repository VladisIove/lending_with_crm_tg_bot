# Generated by Django 3.0.2 on 2020-01-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_auto_20200113_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothesview',
            name='img',
            field=models.ImageField(upload_to='media/', verbose_name='Фотография одежды'),
        ),
    ]
