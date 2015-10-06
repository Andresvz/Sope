# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0002_auto_20150922_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='objeto',
            name='estado',
            field=models.BooleanField(default=0, verbose_name=b'Estado del Articulo'),
        ),
    ]
