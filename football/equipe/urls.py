from . import views
from django.urls import path
from .views import EquipeListCreate, EquipeListView, EquipeCreateView

urlpatterns = [
    path('api/equipes/', EquipeListCreate.as_view(), name='equipe-list-create'),
    path('equipes/', views.equipe_list, name='equipe-list'),
    path('equipes/create/', EquipeCreateView.as_view(), name='equipe-create'),
]