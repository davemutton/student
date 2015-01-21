# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20150121_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='child_pages',
            field=models.ManyToManyField(related_name='child_pages_rel_+', editable=False, to='wiki.Page', blank=True),
            preserve_default=True,
        ),
    ]
