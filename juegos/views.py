from django.shortcuts import render

from .models import Juego,Categoria

# Create your views here.

def index(request):
    juegos= Juego.objects.all()
    context={"juegos":juegos}
    return render (request, 'juegos/index_juegos.html', context)

def crud(request):
    juegos= Juego.objects.all()
    context={"juegos":juegos}
    return render (request, 'juegos/index_juegos.html', context)

def juegosAdd(request):
    if request.method is not "POST":
        juegos= Juego.objects.all()
        context={"juegos":juegos}
        return render (request, 'juegos/index_juegos.html', context)
