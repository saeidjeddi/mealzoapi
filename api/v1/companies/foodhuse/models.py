from django.db import models


class Foodhouse(models.Model):
    shop_name = models.CharField(max_length=64, blank=True, null=True)
    latitude = models.CharField(max_length=64, blank=True, null=True)
    longitude = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    region_state = models.CharField(max_length=64, blank=True, null=True)
    postcode = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    website = models.CharField(max_length=128, blank=True, null=True)
    social_media = models.CharField(max_length=256, blank=True, null=True)
    apps = models.CharField(max_length=256, blank=True, null=True)
    map_url = models.CharField(max_length=256, blank=True, null=True)


    class Meta:
        db_table = 'foodhouse'

    def __str__(self):
        return self.shop_name

