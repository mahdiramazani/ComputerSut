# Generated by Django 4.1.4 on 2023-02-02 07:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0021_checkout_total_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificatesofcourses',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='checkout',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
