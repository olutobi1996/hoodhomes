import os
from django.shortcuts import redirect, render
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET 
from django.views.decorators.cache import cache_page
from .manual_reviews import MANUAL_REVIEWS
from django.http import JsonResponse
from django.core.mail import send_mail, get_connection, BadHeaderError
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
PLACE_ID = os.environ.get("GOOGLE_PLACE_ID")


@cache_page(60*5)
def home(request):
    hero_images = cache.get("hero_images")
    if not hero_images:
        hero_images = [
            "propertyA/Cambridge1.jpg",
            "propertyA/Cambridge2.jpg",
            "propertyA/Cambridge_Photos_5.jpg",
            "propertyA/Cambridge_Photos_8.jpg",
            "propertyA/Cambridge_Photos_7.jpg",
        ]
        cache.set("hero_images", hero_images, 300)

    featured_images = cache.get("featured_images")
    if not featured_images:
        featured_images = [
            "Cambridge1.jpg",
            "Cambridge2.jpg",
            "Cambridge3.jpg",
            "Cambridge4.jpg",
            "Cambridge5.jpg",
            "Cambridge6.jpg",
        ]
        cache.set("featured_images", featured_images, 300)

    return render(request, "core/home.html", {
        "hero_images": hero_images,
        "featured_images": featured_images,
        "PLACE_ID": PLACE_ID,
        "GOOGLE_API_KEY": GOOGLE_API_KEY,
    })



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        consent = request.POST.get("consent", False)

        if not all([name, email, message]):
            messages.error(request, "⚠️ Please fill out all required fields.")
            return redirect("core:contact")

        try:
            # Email to you
            send_mail(
                subject=f"New Contact Form Enquiry from {name}",
                message=(
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Consent: {'Yes' if consent else 'No'}\n\n"
                    f"Message:\n{message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["office@hoodhomes.co.uk"],
                fail_silently=False,
            )

            # Auto-reply
            send_mail(
                subject="Thanks for contacting Hood Homes",
                message=(
                    f"Hi {name},\n\n"
                    "Thanks for getting in touch with Hood Homes. "
                    "We’ve received your enquiry and will respond as soon as possible.\n\n"
                    "— The Hood Homes Team"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=True,
            )

            # ✅ redirect to success page
            return redirect("core:contact_success")

        except Exception as e:
            logger.error(f"Email sending failed: {e}", exc_info=True)
            messages.error(request, "❌ Sorry, there was an error sending your message. Please try again later.")
            return redirect("core:contact")

    return render(request, "core/contact.html")


def contact_success(request):
    """
    Displays a branded success message after form submission.
    Auto-redirects to home after 5 seconds.
    """
    return render(request, "core/contact_success.html")



@require_GET
def google_reviews(request):
    """
    Temporary manual Google reviews
    """
    return JsonResponse({
        "name": "Hood Homes",
        "rating": 5,
        "address": "5 Valiant Lane, Cambridge, CB5 8XB",
        "reviews": MANUAL_REVIEWS
    })


"""
@require_GET
@cache_page(60*30)  # cache for 30 minutes
def google_reviews(request):

    
    if not GOOGLE_API_KEY or not PLACE_ID:
        return JsonResponse({"error": "Missing API key or Place ID"}, status=500)

    url = f"https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": PLACE_ID,
        "fields": "name,rating,reviews,formatted_address",
        "key": GOOGLE_API_KEY
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        return JsonResponse({"error": "Failed to fetch Google reviews", "detail": str(e)}, status=502)

    result = data.get("result", {})
    reviews = result.get("reviews", [])[:5]  # top 5 reviews
    return JsonResponse({
        "name": result.get("name"),
        "rating": result.get("rating"),
        "address": result.get("formatted_address"),
        "reviews": reviews
    })
"""

def about(request):
    return render(request, "core/about.html")

def services(request):
    images = ["11", "12", "13", "14", "15", "16", "17", "18"]
    return render(request, "core/services.html", {"images": images})

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_conditions(request):
    return render(request, 'core/terms_conditions.html')

def cookies_policy(request):
    return render(request, 'core/cookies.html')
