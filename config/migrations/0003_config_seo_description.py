# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='seo_description',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
