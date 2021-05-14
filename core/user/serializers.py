from core.user.models import User
from rest_framework import serializer


class UserSerializer(serializer.ModelSerializer):

    class Meta:
        model = User
        fields = ['public_id', 'username', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active']
