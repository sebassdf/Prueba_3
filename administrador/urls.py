#from django.conf.urls import url 

from django.urls import path
from . import views

urlpatterns = [
    path('index_administrador', views.index, name='index_administrador'),
]
