from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from app.models import Variant, Variantoption, File

def save_variants(request, product):

    try:

        for j  in range(0, len(request.data['details'])):
                
            variation = request.data['details'][j]
            stock = 0
            price = 0
            shipment = 0
            photos = []
            options = []

            for i in range(0, len(variation)):
                
                # Stock
                if i == 0:
                    stock = int(variation[i])

                # Price
                elif i == 1:
                    price = float(variation[i])

                # Shipment
                elif i == 2:
                    shipment = float(variation[i])

                # Photos
                elif i == 3:
                    photos = request.data['photos'][j]

                # Extra variants
                else:
                    options.append({
                        'name': request.data['variations'][i]["name"],
                        'value': variation[i]
                    })

            variant = Variant.objects.create(
                product = product,
                stock = stock,
                price = price,
                shipment = shipment,
            )

            for photo in photos:
                photo_obj = get_object_or_404(File, pk = photo)
                variant.photos.add(photo_obj)

            for option in options:
                variant_option = Variantoption.objects.create(
                    variant = variant,
                    title = option['name'],
                    value = option['value']
                )
                variant_option.save()            

        return Response(status = status.HTTP_201_CREATED)
    
    except Exception as e:

        return Response(status = status.HTTP_400_BAD_REQUEST)