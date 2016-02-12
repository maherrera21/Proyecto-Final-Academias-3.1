from django.contrib import admin

# Register your models here.

from datos.models import *

admin.site.register(Catalogo)
admin.site.register(DatosMadre)
admin.site.register(DefunFetal)
admin.site.register(DefunGeneral)
admin.site.register(DetalleDefFet)
admin.site.register(DetalleDefGen)
