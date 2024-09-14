from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model

class BusinessProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(20)
    logo = models.ImageField(upload_to='business_logo/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.business_name

