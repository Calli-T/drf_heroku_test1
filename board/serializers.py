from dataclasses import field
from rest_framework import serializers
from .models import Auth

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('userId',"password","email")


