# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imovie', '0006_auto_20170526_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereview',
            old_name='movies',
            new_name='movie',
        ),
    ]
