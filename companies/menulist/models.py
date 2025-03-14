from django.db import models

class MenuList(models.Model):
    shop_id = models.CharField(max_length=64)
    shop_name = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.CharField(max_length=32, blank=True, null=True)
    longitude = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    rating = models.CharField(max_length=32, blank=True, null=True)
    total_reviews = models.CharField(max_length=32, blank=True, null=True)
    cuisines = models.CharField(max_length=512, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)
    social_media = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'menulist'

    def __str__(self):
        return self.shop_name