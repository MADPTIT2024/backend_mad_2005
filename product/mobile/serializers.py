from rest_framework import serializers
from .models import Types,Producer , Mobile

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = '__all__'

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'

