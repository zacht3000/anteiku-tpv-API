from anteiku.models import Anteiku
from rest_framework import viewsets, permissions
from .serializers import AnteikuSerializer

class  AnteikuViewSet(viewsets.ModelViewSet):
    queryset = Anteiku.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AnteikuSerializer