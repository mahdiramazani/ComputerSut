# Generated by Django 4.1.4 on 2023-01-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0017_certificatesofcourses_document_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatesofcourses',
            name='image_document',
            field=models.FileField(default=1, upload_to='media/course/document/image'),
            preserve_default=False,
        ),
    ]