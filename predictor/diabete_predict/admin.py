from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Medecin)
class AdminMedecin(admin.ModelAdmin):
    list_display = ['user', 'nom', 'prenom', 'email', 'numero']

@admin.register(Patient)
class AdminPatient(admin.ModelAdmin):
    list_display = ['user', 'nom', 'prenom', 'age']

@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ['designation', 'description', 'posologie', 'heure_de_prise']

@admin.register(Ordonance)
class OrdonanceAdmin(admin.ModelAdmin):
    list_display = ['description', 'get_medicaments', 'date_emission', 'date_validite']  

@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ['date', 'heure', 'patient', 'medecin']

@admin.register(Consultation)
class ConsultaionAdmin(admin.ModelAdmin):
    list_display = ['tension', 'pull']

admin.register(RendezVous)
class AdminRendez(admin.ModelAdmin):
    list_display = ['patient', 'date', 'heure']