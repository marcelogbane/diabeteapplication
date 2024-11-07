# predictor/views.py

from django.shortcuts import render, redirect, get_object_or_404
from joblib import load
import numpy as np
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient
from .forms import *
from datetime import timedelta
from django.shortcuts import render, redirect
from .models import Patient, Medecin
from .forms import RendezVousForm
from django.utils import timezone

def index_rec(request):
   
    patients = Patient.objects.all()[:4]
    today = timezone.now()
    start_of_week = today - timedelta(days=today.weekday())  # Lundi de la semaine
    end_of_week = start_of_week + timedelta(days=6)  # Dimanche de la semaine

    # Récupérer les rendez-vous de la semaine pour le médecin
    try:
        medecin = Medecin.objects.get(user=request.user)
        rendez_vous_semaine = RendezVous.objects.filter(
            medecin=medecin,
            date__range=[start_of_week, end_of_week]
        ).order_by('date')
    except Medecin.DoesNotExist:
        rendez_vous_semaine = []


    if request.method == "POST":
        form = RendezVousForm(request.POST)
        if form.is_valid():
          
            rendez_vous = form.save(commit=False)
            
            try:
                medecin = Medecin.objects.get(user=request.user)
                rendez_vous.medecin_id = medecin.id
                rendez_vous.save()
                return redirect("accueil")
            except Medecin.DoesNotExist:
               
                messages.error(request, "Aucun médecin associé à votre compte.")
                return redirect('login')  

    else:
        form = RendezVousForm()

    return render(request, 'tableaudebordmedecin.html', {'patients': patients, 'form': form, 'rendez_vous_semaine': rendez_vous_semaine})

def RdvDetails(request, rdv_id):
    rdv = get_object_or_404(RendezVous, id=rdv_id)
    return render(request, 'tableaudebordmedecin.html', {'rdv':rdv})


def AnalyseView(request):
    return render(request, 'analyse.html')


def login_user(request):
    """
     fonction de connexion

    """
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")
            return redirect('login')
    
    return render(request, "index1.html")


def logout_user(request):
    """ fonction deconnexion """
    logout(request)
    return redirect('login')

# Charger le modèle
# model = load('diabete_predict\\utils\\utils\\diabetes_model_training.joblib')
model = load('diabete_predict/utils/diabetes_model_training.joblib')

def diabete_analyse(request):
    prediction = None
    prediction_percentage = None
    error_message = None 
    if request.method == 'POST':
        try:
            age = float(request.POST['age'])
            gender = int(request.POST['gender'])  
            hypertension = int(request.POST['hypertension'])  
            heart_disease = int(request.POST['heart_disease'])  
            smoking_history = int(request.POST['smoking_history'])
            bmi = float(request.POST['bmi'])
            HbA1c_level = float(request.POST['HbA1c_level'])
            blood_glucose_level = float(request.POST['blood_glucose_level'])

            # Vérification des valeurs
            if age < 0 or bmi <= 0 or HbA1c_level < 0 or blood_glucose_level < 0:
                error_message = "Veuillez entrer des valeurs valides."
            else:
                input_data = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]])
                
                
                probabilities = model.predict_proba(input_data)[0] 
                prediction_value = model.predict(input_data)[0]

                if prediction_value == 1:
                    prediction = "Diabétique"
                    prediction_percentage = probabilities[1] * 100  # Pourcentage de la classe 1
                else:
                    prediction = "Non Diabétique"
                    prediction_percentage = probabilities[0] * 100  # Pourcentage de la classe 0

        except ValueError as e:
            error_message = "Erreur dans les données d'entrée : " + str(e)

    return render(request, 'analyse.html', {
        'prediction': prediction,
        'prediction_percentage': prediction_percentage,
        'error_message': error_message
    })


