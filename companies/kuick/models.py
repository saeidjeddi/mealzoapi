from django.db import models


class Kuick(models.Model):
    shop_id = models.CharField(max_length=32,)
    shop_name = models.CharField(max_length=256, null=True, blank=True)
    latitude = models.CharField(max_length=64, null=True, blank=True)
    longitude = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    postcode = models.CharField(max_length=32, null=True, blank=True)
    phone =  models.CharField(max_length=64, null=True, blank=True)
    rating = models.CharField(max_length=32, null=True, blank=True)
    total_reviews = models.CharField(max_length=32, null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    keywords = models.CharField(max_length=1024, null=True, blank=True)
    seo_name =  models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        db_table = 'kuick'