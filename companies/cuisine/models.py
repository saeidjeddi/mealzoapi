from django.db import models

class CuisineCategory(models.Model):
    cuisine_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cuisine_name

    class Meta:
        db_table = 'cuisine'