from django.conf.urls import patterns, url

from datos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'inicio/$', views.inicio, name='inicio'),
    url(r'acerca_de/$', views.acerca_de, name='acerca_de'),
    url(r'mapa/$', views.mapa, name='mapa'),
    url(r'defunciones_fetales/$', views.defunciones_fetales, name='defunciones_fetales'),
    url(r'defunciones_generales/$', views.defunciones_generales, name='defunciones_generales'),
)