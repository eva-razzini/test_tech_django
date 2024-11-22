from django.db import models
from django.core.exceptions import ValidationError

class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=100)

    def clean(self):
        if self.joueurs.count() > 11:  # Limiter à 11 joueurs
            raise ValidationError("Une équipe ne peut pas avoir plus de 11 joueurs.")

    def __str__(self):
        return f"{self.nom} ({self.ville})"

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

    def clean(self):
        if self.equipe and self.equipe.joueurs.count() >= 11:
            raise ValidationError("Cette équipe a déjà 11 joueurs, ce qui est le maximum autorisé.")

    def __str__(self):
        return f"{self.nom} - {self.poste}"
