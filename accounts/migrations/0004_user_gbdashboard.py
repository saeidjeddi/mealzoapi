# Generated by Django 5.1.3 on 2025-03-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_getinfo_user_limiteddisplay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gbDashboard',
            field=models.BooleanField(default=False),
        ),
    ]
