from django.db import models

from football.equipe.models import Equipe


class Joueur(models.Model):
    POSTES = [
        ('Gardien', 'Gardien'),
        ('Défenseur', 'Défenseur'),
        ('Milieu', 'Milieu'),
        ('Attaquant', 'Attaquant'),
    ]
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=20, choices=POSTES)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='joueurs')

    def __str__(self):
        return self.nom