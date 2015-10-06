# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0004_auto_20150922_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='objeto',
            name='avatar',
            field=models.ImageField(upload_to=b'imagen/objectos', null=True, verbose_name=b'Imagen del objecto', blank=True),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='estado',
            field=models.BooleanField(default=False, verbose_name=b'Perdido o Encontrado'),
        ),
    ]
