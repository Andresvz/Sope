# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0003_objeto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='estado',
            field=models.BooleanField(default=True, verbose_name=b'Estado del Articulo'),
        ),
    ]
