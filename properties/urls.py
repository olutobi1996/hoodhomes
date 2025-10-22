from django.urls import path
from . import views

app_name = "properties"  # <-- this is the namespace

urlpatterns = [
    path('', views.property_list, name='list'),  # list of properties
]
