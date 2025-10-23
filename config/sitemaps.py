from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'contact', 'services']  # name of your URL patterns

    def location(self, item):
        return reverse(item)

