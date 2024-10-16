from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    whatsapp_link = models.URLField(max_length=200, blank=True, null=True)
    telegram_link = models.URLField(max_length=200, blank=True, null=True)
    tiktok_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
