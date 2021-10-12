from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name