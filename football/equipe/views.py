from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import generics
from .models import Equipe, Joueur
from .serializers import EquipeSerializer
from .forms import JoueurForm
from django.contrib import messages

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

class EquipeListCreate(generics.ListCreateAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class EquipeListView(ListView):
    model = Equipe
    template_name = 'equipes_list.html'
    context_object_name = 'equipes'

class EquipeCreateView(CreateView):
    model = Equipe
    fields = ['nom', 'ville']
    template_name = 'equipe_form.html'
    success_url = reverse_lazy('equipe-list')

def joueurs_list(request):
     joueurs = Joueur.objects.all().order_by('nom')
     return render(request, 'joueurs_list.html', {'joueurs': joueurs})

def joueur_form(request, pk=None):
    if pk:
        joueur = Joueur.objects.get(pk=pk)
    else:
        joueur = None

    if request.method == 'POST':
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            try:
                joueur = form.save(commit=False)
                joueur.full_clean()
                joueur.save()
                messages.success(request, "Le joueur a été sauvegardé avec succès.")
                return redirect('joueurs_list')
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        form.add_error(field, error)
    else:
        form = JoueurForm(instance=joueur)

    return render(request, 'joueur_form.html', {'form': form})
