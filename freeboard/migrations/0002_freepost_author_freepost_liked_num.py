# Generated by Django 4.2.1 on 2023-06-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freepost',
            name='author',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='freepost',
            name='liked_num',
            field=models.IntegerField(default='0'),
        ),
    ]
