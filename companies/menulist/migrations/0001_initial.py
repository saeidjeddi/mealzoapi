# Generated by Django 5.1.3 on 2025-01-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.CharField(max_length=64)),
                ('shop_name', models.CharField(blank=True, max_length=256, null=True)),
                ('latitude', models.CharField(blank=True, max_length=32, null=True)),
                ('longitude', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.CharField(blank=True, max_length=32, null=True)),
                ('total_reviews', models.CharField(blank=True, max_length=32, null=True)),
                ('cuisines', models.CharField(blank=True, max_length=512, null=True)),
                ('url', models.CharField(blank=True, max_length=512, null=True)),
                ('social_media', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('phone', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'menulist',
            },
        ),
    ]
