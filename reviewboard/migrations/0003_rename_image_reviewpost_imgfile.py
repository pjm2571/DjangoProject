# Generated by Django 4.2 on 2023-05-18 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewboard', '0002_reviewpost_author_alter_reviewpost_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewpost',
            old_name='image',
            new_name='imgfile',
        ),
    ]
