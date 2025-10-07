from django.urls import path
from . import views

app_name = "core"  

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
     path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('cookies/', views.cookies_policy, name='cookies'),
    path("api/google-reviews/", views.google_reviews, name="google_reviews"),
]
