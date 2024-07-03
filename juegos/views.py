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
    else:       
        #Es un post , por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla
        id = request.POST["id"]
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        Descripcion = request.POST["Descripcion"]
        id_categoria = request.POST["id_categoria"]
        stock  = request.POST["stock"]
        activo = "1"
        obj=Juego.objects.create(
            id = id,
            nombre = nombre,
            precio = precio,
            Descripcion = Descripcion,
            id_categoria = id_categoria,
            stock = stock,
            activo=1
        )
        obj.save()
        return render(request,"juegos/juegos_add.html",context)
    
def juegos_del(request,pk):
    context = {}
    try:
        juego = Juego.objects.get(rut=pk)

        juego.delete()

        mensaje = "Eliminado satisfactoriamente su producto"
        juegos = Juego.objects.all()
        context = { "juegos": juegos , "mensaje": mensaje }
        return render(request,"juegos/juegos_list.html",context)
    except:
        mensaje = "Error al eliminar el producto"
        juegos = Juego.objects.all()
        context = {"juegos":juegos,"mensaje":mensaje}
        return render("juegos/juegos_list.html", context)
    
def juegos_findEdit(request,pk):
    if pk != "":
        juego=Juego.objects.get(rut=pk)
        #alumno = Alumno.objects.raw(f"SELECT * FROM alumnos_alumno WHERE rut={pk}")

        context = {'juego':juego}

        if juego:
            return render(request,"juegos/juegos_edit.html",context)
        else:
            context={"mensaje":"Error, id no existe"}
            return render(request,"juegos/juegos_edit.html",context)
        
def juegosUpdate(request):
    
    if request.method == "POST":
        print("Entra por aqui si es post")
        id = request.POST["id"]
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        Descripcion = request.POST["Descripcion"]
        id_categoria = request.POST["id_categoria"]
        stock  = request.POST["stock"]

        juego = Juego()
        juego.id = id
        juego.nombre = nombre
        juego.precio = precio
        juego.Descripcion = Descripcion
        juego.id_categoria = id_categoria
        juego.stock =  stock
        juego.activo = 1
        juego.save()

        return render(request, "juegos/juegos_edit.html",context)
    else:
        print("Si no es post")
        #no es un post , entonces se muetra un formulario para hacer un add (insert)
        juegos = Juego.objects.all()
        context = {"juegos":juegos}
        return render(request,"juegos/juegos_list.html",context)
