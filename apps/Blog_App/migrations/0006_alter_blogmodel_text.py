# Generated by Django 4.1.4 on 2023-01-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0005_alter_blogmodel_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='text',
            field=models.TextField(),
        ),
    ]