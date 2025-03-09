from rest_framework import serializers 
from django.contrib.auth.hashers import make_password 
from .models import CustomUser 

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'nickname')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)