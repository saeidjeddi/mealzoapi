# Generated by Django 5.1.3 on 2025-01-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodhub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodhub',
            name='android_link',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='collection_time',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='country',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='delivery_time',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='description',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='merchant_id',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='opening_hours',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='places',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='region',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='review_categories',
        ),
        migrations.RemoveField(
            model_name='foodhub',
            name='twitter',
        ),
        migrations.AddField(
            model_name='foodhub',
            name='city',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='foodhub',
            name='shop_id',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodhub',
            name='shop_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='foodhub',
            name='total_reviews',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
