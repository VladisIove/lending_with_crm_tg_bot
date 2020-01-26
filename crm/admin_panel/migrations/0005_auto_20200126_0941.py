# Generated by Django 3.0.2 on 2020-01-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_auto_20200125_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_novoi_poshti',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
