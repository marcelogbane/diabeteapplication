# predictor/views.py

from django.shortcuts import render, redirect
from joblib import load
import numpy as np
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index_rec(request):
    return render(request, 'tableaudebordmedecin.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index_re')
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")
            return redirect('login')
    
    return render(request, "index1.html")



# Charger le modèle
model = load('diabete_predict\\utils\\utils\\diabetes_model_training.joblib')

def index(request):
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

    return render(request, 'tableaudebordmedecin.html', {
        'prediction': prediction,
        'prediction_percentage': prediction_percentage,
        'error_message': error_message
    })








                    

