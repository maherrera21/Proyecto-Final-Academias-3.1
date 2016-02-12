# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse

from django.template import RequestContext
from django.db.models import *
from datos.models import *
import json
from datos.forms import *

def index(request):
    return render(request, 'index.html')


def acerca_de(request):
    return render(request, 'acerca_de.html')

def mapa(request):
    return render(request, 'mapa.html')

def defunciones_fetales(request):
    """
    """
    context = {'anio_def': None, 'sexo': None, 'sem_gestac': None}

    if request.method=='POST':
        formulario = defun_fetales(request.POST)
    else:
        formulario = defun_fetales()

    context['formulario'] = formulario

    return render(request, 'defunciones_fetales.html', context, context_instance=RequestContext(request))

@csrf_exempt
def funcion_ajax(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        defun_fetales = request.POST.getlist('valor')[0]
        fetales = serializers.serialize('json', DefunFetal.objects.filter(nombre__startswith = defunciones_fetales))
        req['mensaje'] = 'Correcto .... cargando datos '
        req['defun_fetales'] = defun_fetales 
        return JsonResponse(req, safe=False)

def visualizacion1(request):
    """
    """
    defun_fetales = DefunFetal.objects.all()
    datos = []
    for p in fetales:
        datos.append({'label': p.anio_def, 'value': p.sexo, 'value': p.sem_gestac})
    print datos
    datos1 = json.dumps(datos) 
    context = {'datos': datos1}
    return render(request, 'visualizacion1.html', context)


def defunciones_generales(request):
    """
    """
    context = {'sexo': None, 'anio_nac': None, 'anio_def': None}

    if request.method=='POST':
        formulario = defun_generales(request.POST)
    else:
        formulario = defun_generales()

    context['formulario'] = formulario

    return render(request, 'defunciones_generales.html', context, context_instance=RequestContext(request))
