# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_config_seo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='name_Disqus',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
