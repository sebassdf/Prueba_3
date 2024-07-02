from django.shortcuts import render
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def menu(request):
    request.session["usuario"]="donperez"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render (request, 'administrador/menu.html', context)
