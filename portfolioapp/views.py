from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from portfolioapp.forms import VisiteurForm, ContactForm
from portfolioapp.models import Visiteur

# Pour Email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.

# def login(request):
#     #user_list_template = loader.get_template("login.html")
#     context = {}
#     return render(request,'login.html',context)

@login_required
def home(request):
    context ={}
    return render(request, 'homepage.html',context)

def logoutView(request):
    logout(request)
    request.session.clear()
    return redirect('/login')

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
            email = contact.cleaned_data.get('nom')
            poste = contact.cleaned_data.get('poste')
            observations = contact.cleaned_data.get('observations')
            
            # Création d'un nouvel commentaire
            Visiteur.objects.create(nom = email, poste = poste, observations = observations)
            
            # Envoie Email
            # Paramètres de connexion au serveur SMTP
            # smtp_server = 'smtp.gmail.com'
            # smtp_port = 587
            # smtp_username = 'adrientafitasoa@gmail.com'
            # smtp_password = 'votremdp'
            
            # # Adresse e-mail de l'expéditeur
            # sender_email = 'tafitasoarobinson@gmail.com'

            # # Adresse e-mail du destinataire
            # recipient_email = 'adrientafitasoa@gmail.com'

            # # Création de l'objet du message
            # message = MIMEMultipart()
            # message['From'] = sender_email
            # message['To'] = recipient_email
            # message['Subject'] = 'Sujet de l\'e-mail'

            # # Corps du message
            # message_text = 'Contenu de l\'e-mail'
            # message.attach(MIMEText(message_text, 'plain'))

            # # Connexion au serveur SMTP
            # smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            # smtp_connection.starttls()
            # smtp_connection.login(smtp_username, smtp_password)

            # # Envoi de l'e-mail
            # smtp_connection.send_message(message)

            # # Fermeture de la connexion au serveur SMTP
            # smtp_connection.quit()
            
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