# Generated by Django 4.2 on 2023-05-26 10:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewboard', '0003_rename_image_reviewpost_imgfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewpost',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
