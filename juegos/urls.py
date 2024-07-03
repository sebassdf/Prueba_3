#from django.conf.urls import url 

from django.urls import path
from . import views

urlpatterns = [
    path('index_juegos', views.index, name='index_juegos'),
    path('crud', views.crud, name='crud'),
    path('juegosAdd', views.juegosAdd, name='juegosAdd'),
    path('juegos_del/<str:pk>', views.juegos_del, name='juegos_del'),
    path('juegos_findEdit/<str:pk>', views.juegos_findEdit, name='juegos_findEdit'),
    path('juegosUpdate', views.juegosUpdate, name='alumnosUpdate'),



    
]
