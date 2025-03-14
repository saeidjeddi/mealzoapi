# Generated by Django 5.1.3 on 2025-03-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='getInfo',
            new_name='limitedDisplay',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, choices=[('SuperUser', 'SuperUser'), ('Developer', 'Developer'), ('Marketing', 'Marketing'), ('Support', 'Support'), ('Onboarding', 'Onboarding'), ('Management', 'Management'), ('Menu', 'Menu'), ('UX/UI', 'UX/UI')], max_length=255, null=True),
        ),
    ]
