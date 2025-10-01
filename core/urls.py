from django.urls import path
from . import views

app_name = "core"  

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path('privacy-policy/', views.privacy_policy, name='privacy'),
    path('terms-conditions/', views.terms_conditions, name='terms'),
    path('cookies/', views.cookies_policy, name='cookies'),
]
