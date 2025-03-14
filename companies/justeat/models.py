from django.db import models

class Justeat(models.Model):
    shop_id = models.CharField(max_length=16)
    shop_name = models.CharField(max_length=32, null=True, blank=True)
    latitude = models.CharField(max_length=32, null=True, blank=True)
    longitude = models.CharField(max_length=32, null=True, blank=True)
    region = models.CharField(max_length=64, null=True, blank=True)
    county = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=16, null=True, blank=True)
    address = models.CharField(max_length=64, null=True, blank=True)
    postcode = models.CharField(max_length=32, null=True, blank=True)
    rating = models.CharField(max_length=16, null=True, blank=True)
    total_reviews = models.CharField(max_length=16, null=True, blank=True)
    cuisines = models.CharField(max_length=256, null=True, blank=True)


    class Meta:
        db_table = 'justeat'