from rest_framework import serializers
from .models import CustomUser, Iha, Kiralama

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class IhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iha
        fields = '__all__'

class KiralamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kiralama
        fields = '__all__'
