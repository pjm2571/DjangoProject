# Generated by Django 4.2.1 on 2023-06-06 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doglist', '0005_dog_kind_size'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dog',
            new_name='Doglist_Dog',
        ),
    ]
