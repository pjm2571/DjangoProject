# Generated by Django 4.2.1 on 2023-05-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storemap', '0003_alter_store_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='latitude',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='store',
            name='longitude',
            field=models.CharField(default='', max_length=50),
        ),
    ]
