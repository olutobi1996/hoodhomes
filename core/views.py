from django.shortcuts import render
from properties.models import Property
# core/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def home(request):
    featured_images = range(1, 11)  # Creates [1, 2, 3, ... 10]
    return render(request, "core/home.html", {
        "featured_images": featured_images
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        consent = request.POST.get("consent", False)

        if name and email and message:
            # Email that goes to your client
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
                recipient_list=["Office@hoodhomes.co.uk"],  # Client's inbox
                fail_silently=False,
            )

            # Optional auto-reply to the user
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

            messages.success(request, "✅ Thank you for your message. We’ll be in touch soon.")
            return redirect("core:contact")
        else:
            messages.error(request, "⚠️ Please fill out all required fields.")

    return render(request, "core/contact.html")



def about(request):
    return render(request, "core/about.html")

def services(request):
    images = ["11", "12", "13", "14", "15", "16", "17", "18"]
    return render(request, "core/services.html", {"images": images})
