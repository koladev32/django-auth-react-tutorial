from core.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['public_id', 'username', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active']
