from django.db import models


class ScoffableList(models.Model):
    shop_name = models.CharField(max_length=256)
    latitude = models.CharField(max_length=64, null=True, blank=True)
    longitude = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    postcode = models.CharField(max_length=64, null=True, blank=True)
    rating = models.FloatField()
    total_reviews = models.CharField(max_length=64, null=True, blank=True)
    cuisines = models.CharField(max_length=512, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        db_table = 'scoffable'

    def __str__(self):
        return self.shop_name