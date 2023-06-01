"""
__Seed builder__
  Extended module
"""

import json
import seed.routes.opinions as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import Opinion, User, Product
from app.serializers import OpinionSerializer

class OpinionViewSet(SeedRoute.OpinionViewSet):
    

    @action(detail=False, methods=["POST"])
    def last_opinion(self, request): 
        data = request.data
        has_fields_or_400(data, "product", "user")

        user_id = data["user"]
        product_id = data["product"]

        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)
        opinion = Opinion.objects.filter(product__id = product.id, user__id = user.id).first()
          
        if opinion is None:
          return Response(status=200, data={})
        else:
          return Response(status=200, data={ "opinion": OpinionSerializer(opinion, many=False).data })