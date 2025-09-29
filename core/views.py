from django.shortcuts import render
from properties.models import Property

def home(request):
    featured_images = range(1, 11)  # Creates [1, 2, 3, ... 10]
    return render(request, "core/home.html", {
        "featured_images": featured_images
    })


def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, "core/about.html")

def services(request):
    images = ["11", "12", "13", "14", "15", "16", "17", "18"]
    return render(request, "core/services.html", {"images": images})
