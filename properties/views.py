from django.shortcuts import render, get_object_or_404
from .models import Property

# List view
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

# Detail view
def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property_obj})
