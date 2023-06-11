"""
__Seed builder__
  Extended module
"""

import seed.routes.shippings as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import Shipping
from app.serializers import ShippingSerializer

class ShippingViewSet(SeedRoute.ShippingViewSet):
    
    @action(detail=False, methods=['POST'])
    def cancel(self, request):  
        data = request.data
        has_fields_or_400(data, "shippingId")
        shipping_id = data["shippingId"]

        shipping = Shipping.objects.get(id = shipping_id)
        if shipping.status == "CREATED":
            shipping.status = "CANCELED"
            shipping.save()
            return Response(status=200)
        else:
            return Response(status=440)
