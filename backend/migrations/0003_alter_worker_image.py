# Generated by Django 3.2.6 on 2021-10-01 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_booing_date_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
