from django.db import models

class Justeat(models.Model):
    shop_id = models.CharField(max_length=16, unique=True)
    shop_name = models.CharField(max_length=32, blank=True, null=True)
    latitude = models.CharField(max_length=32, blank=True, null=True)
    longitude = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=16, blank=True, null=True)
    area = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    region_state = models.CharField(max_length=64, blank=True, null=True)
    postcode = models.CharField(max_length=32, blank=True, null=True)
    rating = models.CharField(max_length=16, blank=True, null=True)
    total_reviews = models.CharField(max_length=16, blank=True, null=True)
    cuisines = models.CharField(max_length=256, blank=True, null=True)
    unique_name = models.CharField(max_length=32, blank=True, null=True)
    is_new = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'justeat'
