from django.db import models


from django.db import models


class Foodhub(models.Model):
    shop_id = models.CharField(max_length=25)
    shop_name = models.CharField(max_length=128)
    latitude = models.CharField(max_length=64,null=True, blank=True)
    longitude = models.CharField(max_length=64,null=True, blank=True)
    region_state = models.CharField(max_length=64,null=True, blank=True)
    town = models.CharField(max_length=256,null=True, blank=True)
    city = models.CharField(max_length=128,null=True, blank=True)
    street = models.CharField(max_length=128,null=True, blank=True)
    number = models.CharField(max_length=64,null=True, blank=True)
    postcode = models.CharField(max_length=64,null=True, blank=True)
    phone = models.CharField(max_length=64,null=True, blank=True)
    rating = models.CharField(max_length=16,null=True, blank=True)
    total_reviews = models.CharField(max_length=16,null=True, blank=True)
    cuisines = models.CharField(max_length=256,null=True, blank=True)
    url = models.CharField(max_length=128,null=True, blank=True)
    host = models.CharField(max_length=128,null=True, blank=True)
    title = models.CharField(max_length=256,null=True, blank=True)
    keywords = models.CharField(max_length=1024,null=True, blank=True)
    seo = models.CharField(max_length=512,null=True, blank=True)

    class Meta:
        db_table = 'foodhub'

    def __str__(self):
        return self.shop_name
        