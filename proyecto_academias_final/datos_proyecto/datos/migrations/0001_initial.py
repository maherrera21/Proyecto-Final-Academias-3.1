# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
            ],
            options={
                'db_table': 'catalogo',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DatosMadre',
            fields=[
            ],
            options={
                'db_table': 'datos_madre',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefunFetal',
            fields=[
            ],
            options={
                'db_table': 'defun_fetal',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefunGeneral',
            fields=[
            ],
            options={
                'db_table': 'defun_general',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleDefFet',
            fields=[
            ],
            options={
                'db_table': 'detalle_def_fet',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleDefGen',
            fields=[
            ],
            options={
                'db_table': 'detalle_def_gen',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
