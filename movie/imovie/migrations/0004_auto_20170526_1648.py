# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imovie', '0003_auto_20170526_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='movie',
            field=models.ForeignKey(to='imovie.Movie'),
        ),
    ]
