from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
# from .models import User, FullName, Address, Account
from user_model.serializers import UserSerializer, FullNameSerializer, AddressSerializer, AccountSerializer,LoginSerializer

# Create your views here.
class LoginView(viewsets.ViewSet):
    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)