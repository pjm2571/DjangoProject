# Generated by Django 4.2.1 on 2023-06-06 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_dog_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='size',
        ),
    ]
