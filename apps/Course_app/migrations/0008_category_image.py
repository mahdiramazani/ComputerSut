# Generated by Django 4.1.4 on 2022-12-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0007_courseschild_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/category_image'),
        ),
    ]
