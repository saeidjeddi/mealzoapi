from django.db import models




class Orderyoyo(models.Model):
    date = models.DateTimeField()
    shop_id_company = models.CharField(max_length=128, null=True, blank=True)
    shop_url_company = models.CharField(max_length=512, null=True, blank=True)
    shop_name = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=32, null=True, blank=True)
    longitude = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    rating = models.CharField(max_length=16, null=True, blank=True)
    total_reviews = models.CharField(max_length=16, null=True, blank=True)
    cuisines = models.CharField(max_length=512, null=True, blank=True)
    serviceFee = models.CharField(max_length=16, null=True, blank=True)
    deliveryFee = models.CharField(max_length=16, null=True, blank=True)
    deliveryTime = models.CharField(max_length=16, null=True, blank=True)
    takeAwayTime = models.CharField(max_length=16, null=True, blank=True)
    ownerOrContactPerson = models.CharField(max_length=255, null=True, blank=True)
    hasDelivery = models.CharField(max_length=16, null=True, blank=True)


    def __str__(self):
        return self.shop_name
    
    class Meta:
        db_table = 'orderyoyo'
        






