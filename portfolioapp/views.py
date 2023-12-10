from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from portfolioapp.forms import VisiteurForm, ContactForm
from portfolioapp.models import Visiteur

# Create your views here.

# def login(request):
#     #user_list_template = loader.get_template("login.html")
#     context = {}
#     return render(request,'login.html',context)

def home(request):
    context ={}
    return render(request, 'homepage.html',context)

@login_required
def competences(request):
    context ={}
    return render(request, 'competences.html',context)

@login_required
def realisation(request):
    context ={}
    return render(request, 'realisation.html',context)

@login_required
def contact(request):
    if request.method == "POST":
        #Utilisation de Formaulaire
        contact = ContactForm(request.POST)
        
        if contact.is_valid():
            #Acceder au formulaire
            email = contact.cleaned_data.get('email')
            poste = contact.cleaned_data.get('poste')
            observation = contact.cleaned_data.get('observation')
            
            # Création d'un nouvel commentaire
            obs = Visiteur.objects.create(nom = email, poste = poste, observations = observation)
            obs.save()
        else:
            print("Erorr ::: Formulaire ")
        
    context ={}
    return render(request, 'contact.html',context)

@login_required
def loisir(request):
    context ={}
    return render(request, 'loisir.html',context)

def signup(request):
    if request.method == "POST":
        #Utilisation de Formaulaire
        utilisateur = VisiteurForm(request.POST)
        
        if utilisateur.is_valid():
            #Acceder au formulaire
            nom_utilisateur = utilisateur.cleaned_data.get('nom_utilisateur')
            mot_de_passe = utilisateur.cleaned_data.get('mot_de_passe')
            
            # Création d'un nouvel utilisateur
            user = User.objects.create_user(username= nom_utilisateur, password= mot_de_passe)
            
            # Enregistrer les modifications de l'utilisateur
            user.save()
        else :
            print("Erora")
        
    context ={}
    return render(request, 'signup.html',context)