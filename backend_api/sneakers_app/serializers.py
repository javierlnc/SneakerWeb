from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ( 'username', 'first_name', 'last_name', 'email', 'password', 'created_at', 'updated_at')
        reads_only_fields = ('created_at', 'updated_at')