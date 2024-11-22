from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import generics
from .models import Equipe
from .serializers import EquipeSerializer

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class EquipeListCreate(generics.ListCreateAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class EquipeListView(ListView):
    model = Equipe
    template_name = 'equipe_list.html'
    context_object_name = 'equipes'

class EquipeCreateView(CreateView):
    model = Equipe
    fields = ['nom', 'ville']
    template_name = 'equipe_form.html'
    success_url = reverse_lazy('equipe-list')


def equipe_list(request):
    equipes = Equipe.objects.all()
    return render(request, 'equipe_list.html', {'equipes': equipes})