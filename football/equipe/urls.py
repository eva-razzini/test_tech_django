from django.urls import path
from . import views
from .views import EquipeListCreate, EquipeListView, EquipeCreateView

urlpatterns = [
    path('api/equipes/', EquipeListCreate.as_view(), name='equipe-list-create'),
    path('equipes/', EquipeListView.as_view(), name='equipe-list'),
    path('equipes/create/', EquipeCreateView.as_view(), name='equipe-create'),
    path('joueur/create/', views.joueur_form, name='joueur_form'),
    path('joueurs/', views.joueurs_list, name='joueurs_list'),
]