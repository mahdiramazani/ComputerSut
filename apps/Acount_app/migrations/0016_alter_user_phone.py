# Generated by Django 4.1.4 on 2022-12-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0015_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='شماره تلفن'),
        ),
    ]
