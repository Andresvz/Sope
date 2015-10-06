# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0005_auto_20150922_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='categoria',
            field=models.ForeignKey(to='objetos.Categoria'),
        ),
    ]
