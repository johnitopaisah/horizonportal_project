from django.db import models
from business.models import BusinessProfile


class Product(models.Model):
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
