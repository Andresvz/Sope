# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0006_auto_20150925_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='estado',
            field=models.CharField(default=b'perdido', max_length=20, choices=[(b'perdido', b'Perdido'), (b'encontrado', b'Encontrado'), (b'procesado', b'Procesando Entrega')]),
        ),
    ]
