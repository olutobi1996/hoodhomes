from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1  # how many blank image fields by default

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'location', 'price', 'available', 'created_at')
    list_filter = ('service_type', 'available', 'created_at')
    search_fields = ('title', 'location', 'description')
    inlines = [PropertyImageInline]
