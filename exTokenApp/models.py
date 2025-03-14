from django.db import models


class GoogleToken(models.Model):
    access_token = models.TextField()
    refresh_token = models.TextField()

    def __str__(self):
        return self.refresh_token


