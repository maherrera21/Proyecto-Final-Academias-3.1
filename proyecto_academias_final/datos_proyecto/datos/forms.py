#encoding:utf-8 
from django import forms
from django.db.models import*
from datos.models import *

class defun_fetales(forms.Form):

    anio_def = forms.ChoiceField([(y, y) for y in DefunFetal.objects.values('anio_def').distinct().order_by("anio_def")])
    sexo = forms.ChoiceField([(y, y) for y in DefunFetal.objects.values('sexo').distinct().order_by("sexo")])
    sem_gestac= forms.ChoiceField([(y, y) for y in DefunFetal.objects.values('sem_gestac').distinct().order_by("sem_gestac")])

class defun_generales(forms.Form):

    sexo = forms.ChoiceField([(y, y) for y in DefunGeneral.objects.values('sexo').distinct().order_by("sexo")])
    anio_nac = forms.ChoiceField([(y, y) for y in DefunGeneral.objects.values('anio_nac').distinct().order_by("anio_nac")])
    anio_def= forms.ChoiceField([(y, y) for y in DefunGeneral.objects.values('anio_def').distinct().order_by("anio_def")])



    