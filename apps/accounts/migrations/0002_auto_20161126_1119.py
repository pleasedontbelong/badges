# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-26 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='privacy',
            field=models.CharField(choices=[(b'open', 'Open'), (b'registered', 'Registered'), (b'closed', 'Closed')], default=b'open', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy'),
        ),
    ]
