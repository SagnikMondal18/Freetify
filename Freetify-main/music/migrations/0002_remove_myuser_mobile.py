# Generated by Django 5.0.1 on 2024-02-10 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='mobile',
        ),
    ]
