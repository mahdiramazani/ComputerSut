# Generated by Django 4.1.4 on 2022-12-19 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Course_app', '0003_courseschild_link_video_alter_courseschild_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('crested', models.DateTimeField(auto_now_add=True)),
                ('corses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to='Course_app.courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
