# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearningObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('archivefile', models.FileField(upload_to=b'learningobject/archivefiles/%Y/%m/%d')),
                ('indexpath', models.CharField(max_length=254, editable=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100, editable=False, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
