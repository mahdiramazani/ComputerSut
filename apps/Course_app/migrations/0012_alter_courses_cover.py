# Generated by Django 4.1.4 on 2022-12-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0011_courses_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='cover',
            field=models.FileField(upload_to='media/video_cover'),
        ),
    ]