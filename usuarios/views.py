from django.shortcuts import render

from .models import Usuario
from .views import Usuario
# Create your views here.

def index(request):
    usuarios= Usuario.objects.all()
    context={"usuarios":usuarios}
    return render (request, 'usuarios/index.html', context)

def crud(request):
    usuarios= Usuario.objects.all()
    context={"usuarios":usuarios}
    return render (request, 'usuarios/index.html', context)

def home (request):
    context = {}
    return render(request, 'administrador/home.html', context)


