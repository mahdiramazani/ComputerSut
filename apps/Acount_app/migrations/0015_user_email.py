# Generated by Django 4.1.4 on 2022-12-31 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0014_user_is_blogger_user_is_technical_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]