# Generated by Django 5.0 on 2023-12-07 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_event_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='users',
            new_name='user',
        ),
    ]
