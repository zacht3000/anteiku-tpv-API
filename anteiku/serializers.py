from rest_framework import serializers
from .models import Anteiku


class AnteikuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anteiku
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )