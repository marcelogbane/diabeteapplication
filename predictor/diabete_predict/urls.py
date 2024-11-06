from django.urls import path
from .views import *
from .custum_views.views.patient_views import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('analyse_view/', diabete_analyse, name='analyseview'),
    path('analyse/', AnalyseView, name='analyse'),
    path('index/', index_rec, name='accueil'),
    path('ajouter-patient/', add_patient, name='add_patient'),
    path('patient/<int:patient_id>/', patient_detail, name='patient_detail'),
    path('nouvelle-ordonance/', ordonance_view, name='ordonance_view'),
    path('ordonance-details/<int:ordonance_id>', ordonance_detail, name='ordonance_detail'),
    path('details-rendez-vous/<int:rdv_id>', RdvDetails, name='rdv'),


]