# Generated by Django 4.1.4 on 2022-12-21 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0013_courseschild_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
    ]
