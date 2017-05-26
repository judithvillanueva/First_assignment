# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imovie', '0004_auto_20170526_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereview',
            old_name='movie',
            new_name='movies',
        ),
    ]
