from django import forms
from .models import Joueur, Equipe


class JoueurForm(forms.ModelForm):
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Joueur
        fields = ['nom', 'poste', 'equipe']
        widgets = {
            'poste': forms.Select(attrs={'class': 'form-control'}),
            'equipe': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        equipe = cleaned_data.get('equipe')
        if equipe and equipe.joueurs.count() >= 11:
            raise forms.ValidationError("Cette équipe a déjà 11 joueurs, ce qui est le maximum autorisé.")
        return cleaned_data