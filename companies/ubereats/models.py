from django.db import models


class UberEats(models.Model):
    shop_id = models.CharField(max_length=256, null=True, blank=True)
    shop_name = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=64, null=True, blank=True)
    longitude = models.CharField(max_length=64, null=True, blank=True)
    region = models.CharField(max_length=64, null=True, blank=True)
    county = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    postcode = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=64, null=True, blank=True)
    rating = models.CharField(max_length=32, null=True, blank=True)
    total_reviews = models.CharField(max_length=32, null=True, blank=True)
    cuisines = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        db_table = 'ubereats'

    def __str__(self):
        return self.shop_name if self.shop_name else f'Shop {self.shop_id}'