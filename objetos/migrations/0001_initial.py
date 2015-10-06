# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255, verbose_name=b'Nombre de la causa')),
                ('nombre_contacto', models.CharField(max_length=255, verbose_name=b'Nombre de la persona')),
                ('telefono', models.CharField(max_length=255, verbose_name=b'Numero de la persona')),
                ('descripcion', models.TextField(verbose_name=b'descripcion del articulo')),
                ('categoria', models.ManyToManyField(to='objetos.Categoria')),
            ],
        ),
    ]
