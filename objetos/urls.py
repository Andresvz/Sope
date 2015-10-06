from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Main
    url(r'^$', views.HomeView.as_view(), name="index_view"),
    url(r'^objetos/$', views.PerdidoView.as_view(), name="perdidos_view"),
    url(r'^registrar/$', views.EncontraView.as_view(), name="encontrar_view"),
)