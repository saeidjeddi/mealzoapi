from django.db import models


class UberEats(models.Model):
    shop_id = models.CharField(max_length=256, blank=True, null=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=64, blank=True, null=True)
    longitude = models.CharField(max_length=64, blank=True, null=True)
    country  = models.CharField(max_length=16, blank=True, null=True)
    region = models.CharField(max_length=64, blank=True, null=True)
    city_slug = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    street_address = models.CharField(max_length=128, blank=True, null=True)
    region_state = models.CharField(max_length=64, blank=True, null=True)
    postcode = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    rating = models.CharField(max_length=32, blank=True, null=True)
    total_reviews = models.CharField(max_length=32, blank=True, null=True)
    cuisines = models.CharField(max_length=256, blank=True, null=True)
    location_type = models.CharField(max_length=64, blank=True, null=True)
    shop_name_unique = models.CharField(max_length=128, blank=True, null=True)
    class Meta:
        db_table = 'ubereats'

    def __str__(self):
        return self.shop_name if self.shop_name else f'Shop {self.shop_id}'

