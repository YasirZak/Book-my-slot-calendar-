# Generated by Django 5.0.2 on 2024-02-24 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='datetime',
            new_name='date_and_time',
        ),
    ]