from django.db import models


class Foodhub(models.Model):
    shop_id = models.CharField(max_length=25, blank=True, null=True)
    shop_name = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.CharField(max_length=64, blank=True, null=True)
    longitude = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)
    region = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    street = models.CharField(max_length=128, blank=True, null=True)
    number = models.CharField(max_length=64, blank=True, null=True)
    town = models.CharField(max_length=256, blank=True, null=True)
    region_state = models.CharField(max_length=64, blank=True, null=True)
    postcode = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    rating = models.CharField(max_length=16, blank=True, null=True)
    total_reviews = models.CharField(max_length=64, blank=True, null=True)
    cuisines = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=128, blank=True, null=True)
    host = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    opening_hours = models.CharField(max_length=512, blank=True, null=True)
    review_categories = models.CharField(max_length=256, blank=True, null=True)
    merchant_id = models.CharField(max_length=32, blank=True, null=True)
    delivery_time = models.CharField(max_length=32, blank=True, null=True)
    collection_time = models.CharField(max_length=32, blank=True, null=True)
    facebook = models.CharField(max_length=256, blank=True, null=True)
    twitter = models.CharField(max_length=256, blank=True, null=True)
    android_link  = models.CharField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    keywords = models.CharField(max_length=1024, blank=True, null=True)
    seo = models.CharField(max_length=512, blank=True, null=True)


    class Meta:
        db_table = 'foodhub'

    def __str__(self):
        return self.shop_name
