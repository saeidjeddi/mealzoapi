from django.db import models


class TitleLoge(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    website = models.CharField(max_length=256)
    time = models.CharField(max_length=256)
    chengeTime = models.DateTimeField(auto_now_add=True)
    chenge = models.CharField(max_length=300)
    location = models.CharField(max_length=256)


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'google_title_log'
        ordering = ['-chengeTime']




class OpenHoursLoge(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    shop = models.CharField(max_length=256)
    time = models.CharField(max_length=256)
    chengeTime = models.DateTimeField(auto_now_add=True)
    chenge = models.TextField()
    location = models.CharField(max_length=256)


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'google_open_hours_log'
        ordering = ['-chengeTime']



class PhoneLoge(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    shop = models.CharField(max_length=256)
    time = models.CharField(max_length=256)
    chengeTime = models.DateTimeField(auto_now_add=True)
    chenge = models.CharField(max_length=300)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'google_phone_log'
        ordering = ['-chengeTime']




class WebsiteLoge(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    shop = models.CharField(max_length=256)
    time = models.CharField(max_length=256)
    chengeTime = models.DateTimeField(auto_now_add=True)
    chenge = models.CharField(max_length=300)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'google_website_log'
        ordering = ['-chengeTime']
