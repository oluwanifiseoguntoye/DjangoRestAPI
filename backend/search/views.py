from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer
from . import client
from rest_framework.response import Response

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwags):
        query = request.GET.get('q')
        tag = request.GET.get('tag') or None
        if not query:
            return Response('', status=400)
        results = client.perform_search(query, tags=[tag])
        return Response(results)
