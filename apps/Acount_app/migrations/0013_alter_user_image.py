# Generated by Django 4.1.4 on 2022-12-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0012_alter_teacher_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='media/user_image/index.png', null=True, upload_to='media/user_image'),
        ),
    ]
