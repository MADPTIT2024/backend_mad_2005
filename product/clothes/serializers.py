from rest_framework import serializers
from .models import Cloth, Styles, Producer


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class StylesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Styles
        fields = "__all__"


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = "__all__"
