# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Catalogo(models.Model):
    id_catalogo = models.IntegerField(primary_key=True)
    nombre_catalogo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo'


class DatosMadre(models.Model):
    id_datos_madre = models.IntegerField(primary_key=True)
    edad = models.TextField(blank=True, null=True)
    hijos_vivos = models.TextField(blank=True, null=True)
    hijos_nac_vivos = models.TextField(blank=True, null=True)
    hijos_nac_muertos = models.TextField(blank=True, null=True)
    estado_civil = models.TextField(blank=True, null=True)
    etnia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_madre'


class DefunFetal(models.Model):
    id_defun_fetal = models.IntegerField(primary_key=True)
    sexo = models.TextField(blank=True, null=True)
    anio_def = models.IntegerField()
    sem_gestac = models.TextField(blank=True, null=True)
    id_datos_madre = models.ForeignKey(DatosMadre, models.DO_NOTHING, db_column='id_datos_madre')

    class Meta:
        managed = False
        db_table = 'defun_fetal'


class DefunGeneral(models.Model):
    id_defun_general = models.IntegerField(primary_key=True)
    sexo = models.TextField(blank=True, null=True)
    anio_nac = models.TextField(blank=True, null=True)
    anio_def = models.IntegerField(blank=True, null=True)
    edad = models.TextField(blank=True, null=True)
    cod_edad = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'defun_general'


class DetalleDefFet(models.Model):
    id_detalle_def_fet = models.IntegerField(primary_key=True)
    nombre_detalle_fet = models.TextField(blank=True, null=True)
    id_catalogo = models.ForeignKey(Catalogo, models.DO_NOTHING, db_column='id_catalogo')
    id_defun_fetal = models.ForeignKey(DefunFetal, models.DO_NOTHING, db_column='id_defun_fetal')

    class Meta:
        managed = False
        db_table = 'detalle_def_fet'


class DetalleDefGen(models.Model):
    id_detalle_def_gen = models.IntegerField(primary_key=True)
    nombre_detalle_gen = models.TextField(blank=True, null=True)
    id_catalogo = models.ForeignKey(Catalogo, models.DO_NOTHING, db_column='id_catalogo')
    id_defun_general = models.ForeignKey(DefunGeneral, models.DO_NOTHING, db_column='id_defun_general')

    class Meta:
        managed = False
        db_table = 'detalle_def_gen'

