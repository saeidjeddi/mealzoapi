from django.db import models


class Foodhouse(models.Model):
    shop_name = models.CharField(max_length=64, null=True, blank=True)
    latitude =  models.CharField(max_length=64, null=True, blank=True)
    longitude =  models.CharField(max_length=64 , null=True, blank=True)
    address  =  models.CharField(max_length=128 , null=True, blank=True)
    region_state = models.CharField(max_length=64 , null=True, blank=True)
    postcode  = models.CharField(max_length=32 , null=True, blank=True)
    phone = models.CharField(max_length=64 , null=True, blank=True)
    website =  models.CharField(max_length=128 , null=True, blank=True)
    social_media = models.CharField(max_length=256 , null=True, blank=True)
    map_url   =  models.CharField(max_length=256 , null=True, blank=True)
    app_store_link  = models.CharField(max_length=255 , null=True, blank=True)
    android_link  =  models.CharField(max_length=255 , null=True, blank=True)


    class Meta:
        db_table = 'foodhouse'

    def __str__(self):
        return self.shop_name
