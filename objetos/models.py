from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=255, verbose_name="Nombre de la categoria",)

	def __unicode__(self):
		return self.nombre


ESTILOS_CHOICES = (
   ('perdido', 'Objeto Perdido'),
   ('encontrado', 'Objeto Entregado'),
   ('procesado', 'Objeto en proceso de entrega'),
)

class Objeto(models.Model):
	titulo = models.CharField(max_length=255, verbose_name="Nombre de la causa",)
	nombre_contacto = models.CharField(max_length=255, verbose_name="Nombre de la persona",)
	telefono = models.CharField(max_length=255, verbose_name="Numero de la persona",)
	descripcion = models.TextField(verbose_name="descripcion del articulo",)
	estado = models.CharField(max_length=20, choices=ESTILOS_CHOICES, default='perdido')
	avatar = models.ImageField(upload_to="imagen/objectos", null=True, blank=True, verbose_name="Imagen del objecto")
	categoria =  models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.titulo