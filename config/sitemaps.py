from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from properties.models import Property


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'contact', 'services']  # name of your URL patterns

    def location(self, item):
        return reverse(item)

# Optional: if you have dynamic models like properties
class PropertySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Property.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()  # make sure your model has this
