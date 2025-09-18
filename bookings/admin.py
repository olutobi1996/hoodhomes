from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service_type', 'created_at')
    list_filter = ('service_type', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
