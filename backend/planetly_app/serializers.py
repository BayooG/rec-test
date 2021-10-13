from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import fields, serializers
from planetly_app.models import UsageType, Usage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UsageTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsageType
        fields = ['id', 'name', 'unit', 'factor']
        
class UsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usage
        fields = ['id', 'user', 'usage_type', 'usage_at', 'amount']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

            
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")