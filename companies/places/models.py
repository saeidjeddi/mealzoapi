from django.db import models

class City(models.Model):
    areacd = models.TextField(primary_key=True)
    areanm = models.TextField(blank=True, null=True)
    parentcd = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.areacd

    class Meta:
        db_table = 'cities'



class Region(models.Model):
    value = models.CharField(max_length=20)
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.value

    class Meta:
        db_table = 'region'