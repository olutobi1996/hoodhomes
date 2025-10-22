# models.py
from django.db import models

class Property(models.Model):
    SERVICE_CHOICES = [
        ('sales', 'Sales'),
        ('lettings', 'Lettings'),
        ('investment', 'Investment'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=255)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.location})"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="properties/")
    order = models.PositiveIntegerField(default=0)  # optional: control image order

    def __str__(self):
        return f"Image for {self.property.title}"
