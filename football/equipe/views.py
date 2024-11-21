from rest_framework import viewsets
from .models import Equipe
from .serializers import EquipeSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer