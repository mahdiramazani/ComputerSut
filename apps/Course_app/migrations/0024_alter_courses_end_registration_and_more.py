# Generated by Django 4.1.4 on 2023-02-05 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0023_courses_end_registration_courses_start_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='end_registration',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 10, 18, 0, 50, 420331, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='start_registration',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 5, 18, 0, 50, 420331, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
