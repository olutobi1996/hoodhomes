import os
from django.shortcuts import redirect, render
from properties.models import Property
# core/views.py
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

def home(request):
    featured_images = range(1, 11)  # Creates [1, 2, 3, ... 10]
    return render(request, "core/home.html", {
    "featured_images": featured_images,
    "PLACE_ID": PLACE_ID,
    "GOOGLE_API_KEY": GOOGLE_API_KEY,
})



logger = logging.getLogger(__name__)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message_text = request.POST.get("message", "").strip()
        consent = request.POST.get("consent") == "on"

        if not (name and email and message_text):
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"error": "⚠️ Please fill out all required fields."})
            messages.error(request, "⚠️ Please fill out all required fields.")
            return redirect("/#contact-form")

        client_subject = f"New Contact Form Enquiry from {name}"
        client_message = (
            f"Name: {name}\nEmail: {email}\nPhone: {phone}\nConsent: {'Yes' if consent else 'No'}\n\nMessage:\n{message_text}"
        )
        user_subject = "Thanks for contacting Hood Homes"
        user_message = (
            f"Hi {name},\n\nThanks for getting in touch with Hood Homes. "
            "We’ve received your enquiry and will respond as soon as possible.\n\n— The Hood Homes Team"
        )

        try:
            send_mail(
                subject=client_subject,
                message=client_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["office@hoodhomes.co.uk"],
                fail_silently=False,
            )

            send_mail(
                subject=user_subject,
                message=user_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=True,
            )

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": "✅ Thank you for your message. We’ll be in touch soon."})

            messages.success(request, "✅ Thank you for your message. We’ll be in touch soon.")
            return redirect("/#contact-form")

        except BadHeaderError:
            logger.exception("BadHeaderError in contact form")
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"error": "⚠️ Invalid header found in email."})
            messages.error(request, "⚠️ Invalid header found in email.")
        except Exception as e:
            logger.exception("Error sending contact form email: %s", e)
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"error": "⚠️ Something went wrong. Please try again later."})
            messages.error(request, "⚠️ Something went wrong. Please try again later.")
            return redirect("/#contact-form")

    return render(request, "core/contact.html")



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
