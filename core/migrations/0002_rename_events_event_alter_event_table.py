# Generated by Django 5.0 on 2023-12-07 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.AlterModelTable(
            name='event',
            table='event',
        ),
    ]
