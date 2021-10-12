from django.conf import settings
from django.db import models



class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    longitude = models.CharField(verbose_name='Longitude',max_length=100,null=True)
    latitude = models.CharField(verbose_name='Latitude',max_length=100,null=True)
    captcha_score = models.FloatField(default=0.0)
    has_profile = models.BooleanField(default=False)


    def __str__(self):
        return self.user

