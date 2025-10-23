from django.urls import path
from . import views

app_name = "properties"  # fine to keep this namespace

urlpatterns = [
    path('', views.gallery, name='gallery'),  # renamed to gallery
]
