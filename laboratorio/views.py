from django.shortcuts import render, redirect
from .models import Laboratorio, DirectorGeneral, Producto
from .forms import LaboratorioForm, DirectorGeneralForm, ProductoForm
from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime

from django.http import HttpResponse , HttpResponseRedirect
from django.views.generic import TemplateView
import datetime
from .forms import InputForm, BoardsForm, RegistroUsuarioForm
from tokenize import PseudoExtras
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http.response import JsonResponse

# Create your views here.
def Bienvenido(request):
    context = {}
    return render(request, 'bienvenido.html', context)

def Primero(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'primero.html', {'laboratorios': laboratorios})

def editar_laboratorio_view(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('/primero')  
    else:
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'editar-laboratorio.html', {'form': form})

def agregar_laboratorio_view(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('primero')
    else:
        form = LaboratorioForm()
    
    return render(request, 'agregar-laboratorio.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión.")
    return HttpResponseRedirect('/')

def eliminarlaboratorio_view(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)  
    laboratorio.delete()
    messages.success(request, 'Laboratorio Eliminado') 
    return redirect('/primero')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como : {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado.")
            return HttpResponseRedirect('/')
    
        messages.error(request, "Registro invalido.")
    form = RegistroUsuarioForm()
    context = { "register_form" : form }
    return render(request, "registro.html", context)