from django.db import models

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('valuation', 'Valuation'),
        ('sales', 'Sales Enquiry'),
        ('lettings', 'Lettings Enquiry'),
        ('investment', 'Investment Enquiry'),
        ('general', 'General Enquiry'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"
