# Generated by Django 5.0.2 on 2024-03-15 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_calendar_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='Samgatha', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AdminUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]