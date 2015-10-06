from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Objeto

class HomeView(TemplateView):
    template_name = 'index.html'

    

class PerdidoView(TemplateView):
	template_name = 'objectos.html'

	def get_context_data(self, **kwargs):
		context = super(PerdidoView, self).get_context_data(**kwargs)
		context['objetos'] = Objeto.objects.all()
		return context


class EncontraView(TemplateView):
	template_name = 'encontraste.html'