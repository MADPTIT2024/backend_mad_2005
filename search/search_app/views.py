# Trong file views.py của ứng dụng search
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


def get_product_type(type_product):
    if type_product == "book":
        return 1
    elif type_product == "cloth":
        return 2
    elif type_product == "mobile":
        return 3
    else:
        return None


class ProductSearchAPIView(APIView):
    def get(self, request, type_product):
        keyword = request.GET.get("keyword", "")
        product_url = get_product_type(type_product)
        url = f"http://localhost:800{product_url}/{type_product}s/search?keyword={keyword}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            return Response(data)
        else:
            return Response(
                {"error": "Failed to fetch data"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
