from django.shortcuts import render

from .models import Usuario

# Create your views here.

def index(request):
    usuarios= Usuario.objects.all()
    context={"usuarios":usuarios}
    return render (request, 'usuarios/index.html', context)





