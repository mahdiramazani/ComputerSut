# Generated by Django 4.1.4 on 2023-01-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0016_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]
