from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Página principal")
    context = {
        "titulo": "Home",
    }
    return render(request, "home.html", context)

def reclamos(request):
    #return HttpResponse("Página reclamos")
    context = {
        "titulo": "Reclamos"
    }
    return render(request, "reclamos.html", context)

def productos(request):
    #return HttpResponse("Página reclamos")
    context = {
        "titulo": "Productos",
        "productos": ["producto 1", "producto 2", "producto 3"]
    }
    return render(request, "productos.html", context)