from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
class Medecin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=70)
    numero = PhoneNumberField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Medicament(models.Model):
    designation = models.CharField(max_length=150)
    description = models.TextField()
    posologie = models.TextField()
    heure_de_prise = models.TimeField()

    def __str__(self):
        return f'{self.designation}'

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=70)
    email = models.EmailField("Adresse mail", max_length=254)
    age = models.CharField(max_length=50)
    genre = models.CharField("Genre", max_length=50, choices=(('F', 'Femme'), ('M', 'Homme')))
    hypertention = models.CharField("Hypertention", max_length=50, choices=(('oui', 'Oui'), ('non', 'Non')))
    maladie_cardiaque = models.CharField("Maladie Cardiaque", max_length=50, choices=(('oui', 'Oui'), ('non', 'Non')))
    numero = PhoneNumberField()
    masse = models.FloatField()
    taille = models.FloatField()
    imc = models.FloatField(blank=True, null=True)  
    etat = models.CharField("Etat", max_length=50, choices=(('N', "Normale"), ('I', 'Intermediaire'), ('U', 'Urgent')))
    medecin = models.ForeignKey(Medecin, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

    @property
    def imc_calcul(self):
        """Calculer l'IMC."""
        if self.taille > 0:
           self.imc = round(self.masse / (self.taille ** 2), 2)
        return 0

class Ordonance(models.Model):
    description = models.TextField()
    medicaments = models.ManyToManyField(Medicament)
    date_emission = models.DateField(auto_now_add=True)
    date_validite = models.DateField()
    patient = models.ForeignKey(Patient, related_name='ordonances', on_delete=models.CASCADE)

    def get_medicaments(self):
        return ", ".join([medicament.designation for medicament in self.medicaments.all()])
    get_medicaments.short_description = 'Médicaments'


class Consultation(models.Model):
        date = models.DateField(auto_now_add=True)
        tension = models.FloatField()
        pull = models.FloatField()
        masse = models.FloatField()
        observation = models.TextField()
        patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)


class RendezVous(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    medecin = models.ForeignKey(Medecin, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('date', 'heure', 'patient', 'medecin')
