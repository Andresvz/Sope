# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objeto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='objeto',
            name='categoria',
            field=models.OneToOneField(default=1, to='objetos.Categoria'),
            preserve_default=False,
        ),
    ]
