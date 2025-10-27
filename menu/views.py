from django.shortcuts import render, redirect
from .models import Reserva

# Create your views here.

def home(request):
    reservas = Reserva.objects.all()
    return render(request,"index.html",{"reservas":reservas})

def login(request):
    return render(request,"login.html")

def lista(request):
    vlogin = request.POST.get("login")
    vsenha = request.POST.get("senha")
    if vlogin == "admin" and vsenha == "admin":
        reservas = Reserva.objects.all()
        return render(request,"lista.html",{"reservas":reservas})
    else:
        reservas = Reserva.objects.all()
        return render(request,"index.html",{"reservas":reservas})
    
def salvar(request):
    vnome = request.POST.get("nome")
    vemail = request.POST.get("email")
    vtelefone = request.POST.get("telefone")
    vqtd = request.POST.get("qtd")
    vdata = request.POST.get("data")
    Reserva.objects.create(nome=vnome,telefone=vtelefone,email=vemail,qtd=vqtd,data=vdata)
    reservas = Reserva.objects.all()
    return render(request,"index.html",{"reservas":reservas})

def delete(request, id):
    reserva = Reserva.objects.get(id = id)
    reserva.delete()
    reservas = Reserva.objects.all()
    return render(request,"lista.html",{"reservas":reservas})

def editar(request, id):
    reserva = Reserva.objects.get(id = id)
    return render(request,"update.html",{"reserva":reserva})

def update(request, id):
    vnome = request.POST.get("nome")
    vemail = request.POST.get("email")
    vtelefone = request.POST.get("telefone")
    vqtd = request.POST.get("qtd")
    vdata = request.POST.get("data")
    reserva = Reserva.objects.get(id = id)
    reserva.nome = vnome
    reserva.email = vemail
    reserva.telefone = vtelefone
    reserva.qtd = vqtd
    reserva.data = vdata
    reserva.save()
    reservas = Reserva.objects.all()
    return render(request,"lista.html",{"reservas":reservas})