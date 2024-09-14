from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModolSerializer):
    class Meta:
        model = User
        field = ['id', 'username', 'email']
