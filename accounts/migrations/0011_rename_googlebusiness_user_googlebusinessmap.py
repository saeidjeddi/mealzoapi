# Generated by Django 5.1.3 on 2025-03-12 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_device_user_devices_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='googleBusiness',
            new_name='googleBusinessMap',
        ),
    ]
