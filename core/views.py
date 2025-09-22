from django.shortcuts import render
from properties.models import Property

def home(request):
    properties = Property.objects.filter(available=True)[:6]  # latest 6 properties
    return render(request, 'core/home.html', {'properties': properties})


def contact(request):
    return render(request, 'core/contact.html')


def about(request):
    return render(request, "core/about.html")
