from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'nom', 
            'prenom', 
            'email', 
            'age', 
            'genre', 
            'hypertention', 
            'maladie_cardiaque', 
            'numero', 
            'masse', 
            'taille', 
            'etat'
        ]


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['tension', 'pull', 'masse', 'observation', 'patient']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'observation': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tension"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )

        self.fields["pull"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )   

        self.fields["masse"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )

        self.fields["observation"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )

        self.fields["patient"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )


class OrdonanceForm(forms.ModelForm):
    class Meta:
        model = Ordonance
        fields = ['date_validite', 'patient', 'medicaments', 'description']
        widgets = {
            'date_validite': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date_validite"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )

        self.fields["patient"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )   

        self.fields["medicaments"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )

        self.fields["description"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['date', 'heure', 'patient']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )

        self.fields["heure"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )       

        self.fields["patient"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )       
          

