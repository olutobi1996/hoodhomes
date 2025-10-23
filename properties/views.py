from django.shortcuts import render

def gallery(request):
    # Property A — now includes Cambridge + Knightly Avenue
    propertyA_images = [
        f"images/gallery/propertyA/{filename}"
        for filename in [
            # Cambridge images
            "Cambridge_Photos_5.jpg",
            "Cambridge_Photos_8.jpg",
            "Cambridge_Photos_14.jpg",
            "Cambridge_Photos_17.jpg",
            "Cambridge_Photos_23.jpg",
            "Cambridge_Photos_26.jpg",
            "Cambridge_Photos_27.jpg",
            "Cambridge_Photos_28.jpg",
            "Cambridge_Photos_32.jpg",
            "Cambridge_Photos_35.jpg",
            "35_Knightly_Avenue_1.jpg",
            "35_Knightly_Avenue_2.jpg",
            "35_Knightly_Avenue_3.jpg",
            "35_Knightly_Avenue_10.jpg",
            "35_Knightly_Avenue_13.jpg",
            "35_Knightly_Avenue_15.jpg",
            "35_Knightly_Avenue_16.jpg",
            "35_Knightly_Avenue_25.jpg",
            "35_Knightly_Avenue_27.jpg",
        ]
    ]

    # Property B — now includes Hillfield + Cambridge (swapped correctly)
    propertyB_images = [
        f"images/gallery/propertyB/{filename}"
        for filename in [
            # Hillfield images
            "48_Hillfield_Comberton_3.jpg",
            "48_Hillfield_Comberton_4.jpg",
            "48_Hillfield_Comberton_23.jpg",
            "48_Hillfield_Comberton_28.jpg",
            "48_Hillfield_Comberton_29.jpg",
            "48_Hillfield_Comberton_32.jpg",
            "48_Hillfield_Comberton_35.jpg",
            "48_Hillfield_Comberton_37.jpg",
            "48_Hillfield_Comberton_39.jpg",
            "48_Hillfield_Comberton_41.jpg",
            "48_Hillfield_Comberton_43.jpg",
            "48_Hillfield_Comberton_45.jpg",
        ]
    ]

    context = {
        "propertyA_images": propertyA_images,
        "propertyB_images": propertyB_images,
    }

    return render(request, "properties/gallery.html", context)
