# Generated by Django 5.0.2 on 2024-03-15 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_event_duration_event_venue_adminusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='admin_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.adminusers'),
        ),
    ]