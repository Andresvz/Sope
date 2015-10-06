from django.contrib import admin
from .models import Objeto, Categoria
from django.contrib.auth.models import Group, User


class ObjectoAdmin(admin.ModelAdmin):
	list_display= ('image_display','titulo','nombre_contacto','telefono','descripcion','retornar','estado',)
	list_display_links  = ('titulo',)
	list_editable = ('estado',)
	list_filter = ('titulo','nombre_contacto','telefono','descripcion','estado',)
	search_fields = ('titulo',)
	
	
	def retornar(self, obj):
		return obj.categoria.nombre
	retornar.short_description = 'Categorias'

	def image_display(self, obj):
	    if obj.avatar:
	        return '<img src="%s" width="120px" height="120px">' % (obj.avatar.url)
	    else:
	        return '<img src="%s" width="120px" height="120px">' % ('http://placehold.it/60x60')
	image_display.allow_tags = True
	image_display.admin_order_field = 'Imagen del Objecto'
	image_display.short_description = 'Imagen del Objecto'
	
# admin.site.unregister(User,)
admin.site.unregister(Group,)
admin.site.register(Objeto, ObjectoAdmin)
admin.site.register(Categoria,)
