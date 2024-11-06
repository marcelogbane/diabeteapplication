from celery import shared_task
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone
from .models import RendezVous
from django.conf import settings

@shared_task
def envoyer_rappel_rdv():
    # Calcule de la date et l'heure actuelles
    maintenant = timezone.now()

    # Récupération de tous les rendez-vous à rappeler (5 minutes avant)
    rendez_vous_a_rappeler = RendezVous.objects.filter(date__gt=maintenant, date__lte=maintenant + timedelta(minutes=5))

    for rdv in rendez_vous_a_rappeler:
        # Envoi du message de rappel pour le patient et le médecin
        patient_email = rdv.patient.email
        medecin_email = rdv.medecin.email
        
        # Message pour le patient
        send_mail(
            'Rappel de votre rendez-vous médical',
            f'Bonjour {rdv.patient.nom},\n\nCe message est pour vous rappeler votre rendez-vous prévu dans 5 minutes, à {rdv.date}.',
            settings.EMAIL_HOST_USER,
            [patient_email],
            fail_silently=False,
        )

        # Message pour le médecin
        send_mail(
            'Rappel de votre rendez-vous médical',
            f'Bonjour Dr {rdv.medecin.nom},\n\nCe message est pour vous rappeler le rendez-vous avec votre patient {rdv.patient.nom} prévu dans 5 minutes, à {rdv.date}.',
            settings.EMAIL_HOST_USER,
            [medecin_email],
            fail_silently=False,
        )

# jour du rdv

@shared_task
def envoyer_rappel_rdv_aujourdhui():
    # Calcule de la date et l'heure actuelles
    maintenant = timezone.now()

    # Récupération des rendez-vous à rappeler (2 minutes avant)
    rendez_vous_a_rappeler = RendezVous.objects.filter(date__date=maintenant.date(), date__gt=maintenant, date__lte=maintenant + timedelta(minutes=2))

    for rdv in rendez_vous_a_rappeler:
        # Envoi du message de rappel pour le patient et le médecin
        patient_email = rdv.patient.email
        medecin_email = rdv.medecin.email
        
        # Message pour le patient
        send_mail(
            'Rappel de votre rendez-vous médical',
            f'Bonjour {rdv.patient.nom},\n\nCe message est pour vous rappeler votre rendez-vous prévu dans 2 minutes, à {rdv.date}.',
            settings.EMAIL_HOST_USER,
            [patient_email],
            fail_silently=False,
        )

        # Message pour le médecin
        send_mail(
            'Rappel de votre rendez-vous médical',
            f'Bonjour Dr {rdv.medecin.nom},\n\nCe message est pour vous rappeler le rendez-vous avec votre patient {rdv.patient.nom} prévu dans 2 minutes, à {rdv.date}.',
            settings.EMAIL_HOST_USER,
            [medecin_email],
            fail_silently=False,
        )