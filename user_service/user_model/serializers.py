from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, FullName, Address, Account

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    fullname = FullNameSerializer()
    address = AddressSerializer()
    account = AccountSerializer()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')
        account_data = validated_data.pop('account')

        fullname = FullName.objects.create(**fullname_data)
        address = Address.objects.create(**address_data)
        account = Account.objects.create(**account_data)

        user = User.objects.create(fullname=fullname, address=address, account=account)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            try:
                account = Account.objects.get(username=username)
                if account.password == password:
                    user = User.objects.get(account=account)
                    return user
                else:
                    raise serializers.ValidationError("Incorrect password.")
            except Account.DoesNotExist:
                raise serializers.ValidationError("Account does not exist.")
        else:
            raise serializers.ValidationError("Both username and password are required.")

