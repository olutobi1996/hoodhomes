from django.shortcuts import render, get_object_or_404
from .models import Property

def property_list(request):
    # Images for Property A
    propertyA_images = [f'images/properties/propertyA/{i}.jpg' for i in range(1, 31)]
    # Images for Property B
    propertyB_images = [f'images/properties/propertyB/{i}.jpg' for i in range(1, 31)]

    context = {
        'propertyA_images': propertyA_images,
        'propertyB_images': propertyB_images,
    }
    return render(request, 'properties/property_list.html', context)


