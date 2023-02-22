from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

# Create your views here.

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """Django Rest Framework API View"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invlaid": "Invalid Data"}, status=400)
