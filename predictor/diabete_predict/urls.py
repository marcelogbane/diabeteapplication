from django.urls import path
from .views import login_user, index_rec

urlpatterns = [
    path('', login_user, name='login'),
    path('indexdashboard/', index_rec, name='index_re'),
]