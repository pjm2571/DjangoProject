# Generated by Django 4.2.1 on 2023-06-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewboard', '0006_alter_reviewpost_like_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewpost',
            name='like_user',
        ),
        migrations.AddField(
            model_name='reviewpost',
            name='liked_num',
            field=models.CharField(default='0', max_length=50, null=True),
        ),
    ]
