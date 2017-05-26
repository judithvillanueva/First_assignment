# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imovie', '0005_auto_20170526_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='city',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='country',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='state',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
