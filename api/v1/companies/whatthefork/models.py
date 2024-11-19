from django.db import models


class WhatTheFork(models.Model):
    shop_id = models.CharField(max_length=16, unique=True)
    shop_name = models.CharField(max_length=32, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    region = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=16, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    region_state = models.CharField(max_length=64, blank=True, null=True)
    postcode = models.CharField(max_length=16, blank=True, null=True)
    phone  = models.CharField(max_length=16, blank=True, null=True)
    rating = models.CharField(max_length=16, blank=True, null=True)
    total_reviews = models.CharField(max_length=16, blank=True, null=True)
    cuisines = models.CharField(max_length=100, blank=True, null=True)
    url_map = models.CharField(max_length=64, blank=True, null=True)
    map_preview_url = models.CharField(max_length=64, blank=True, null=True)
    about_text = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    email_business = models.CharField(max_length=32, blank=True, null=True)
    unique_name = models.CharField(max_length=32, blank=True, null=True)
    instagram_url = models.CharField(max_length=64, blank=True, null=True)
    facebook_url = models.CharField(max_length=64, blank=True, null=True)
    twitter_url = models.CharField(max_length=64, blank=True, null=True)
    google_play_link = models.CharField(max_length=64, blank=True, null=True)
    app_store_link = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    main_text = models.CharField(max_length=255, blank=True, null=True)
    opening_hours_readable = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'whatthefork'

