from django.shortcuts import render

def create_booking(request):
    return render(request, 'bookings/create.html')
