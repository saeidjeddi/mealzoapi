from django.db import models

class PostCodes(models.Model):
    Postcode = models.TextField(primary_key=True)

    def __str__(self):
        return self.Postcode

    class Meta:
        db_table = 'postcodes'