from django.shortcuts import render, redirect, get_object_or_404
from ...forms import *
from diabete_predict.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import random
from django.conf import settings
from twilio.rest import Client

from django.contrib.auth.models import User

# SAQ99Z7JS6FZW6TFQLFA39DT

@login_required
def add_patient(request):
    try:
        medecin = Medecin.objects.get(user=request.user)
    except Medecin.DoesNotExist:
        return HttpResponseForbidden("Vous devez être un médecin pour ajouter un patient.")
    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            random_digits = random.randint(100, 999)
            username = f"{patient.nom}{random_digits}"
            password = "sek20is04"

            
            user = User.objects.create_user(username=username, password=password)
            user.save()

            
            patient.user = user
            patient.medecin = medecin  
            patient.save()

             # Envoi du SMS avec les identifiants
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message = client.messages.create(
            body=f"Bonjour {patient.nom}, vos identifiants sont :\nNom d'utilisateur : {username}\nMot de passe : {password}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=str(patient.numero) 
        )

            return redirect('accueil') 
    else:
        form = PatientForm()
    
    return render(request, 'add_patient.html', {'form': form})



def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    consultation = Consultation.objects.filter(patient=patient_id)
    ordonance = Ordonance.objects.filter(patient=patient_id)

    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil') 
    else:
        form = ConsultationForm()
    return render(request, 'patient_detail.html', {'patient': patient, 
                                                   'form':form, 
                                                   'consultation':consultation,
                                                   'ordonances':ordonance
                                                   })


def ordonance_view(request):
    if  request.method == 'POST':
        form = OrdonanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')

    else:
        form = OrdonanceForm()

    return render(request, 'ordonance.html', {'form':form})       


def ordonance_detail(request, ordonance_id):
    ordonance = get_object_or_404(Ordonance, id=ordonance_id)
    return render(request, 'ordonance_details.html', {
        'ordonance':ordonance
    })


# def RendezVous_View(request):
#     if request.method == "POST":
#         form = RendezVousForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("acceuil")

#     else:
#         form = RendezVousForm()

#     return render(request, 'tableaudebordmedecin.html', {'form':form})        
    



