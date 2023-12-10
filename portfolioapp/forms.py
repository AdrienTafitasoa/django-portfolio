from django import forms

class VisiteurForm(forms.Form):
    nom_utilisateur = forms.CharField(max_length=50, error_messages={'required': 'Champs obligatoire'})
    mot_de_passe = forms.CharField(max_length=50, error_messages={'required': 'Champs obligatoire'})
    
class ContactForm(forms.Form):
    nom = forms.CharField(max_length=50, error_messages={'required': 'Champs obligatoire'})
    poste = forms.CharField(max_length=50, error_messages={'required': 'Champs obligatoire'})
    observations = forms.CharField(max_length=250, error_messages={'required': 'Champs obligatoire'})
