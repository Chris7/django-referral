# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='end_date',
            field=models.DateTimeField(help_text='The date when this campaign will end', null=True, verbose_name='Expiration Date', blank=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='start_date',
            field=models.DateTimeField(help_text='The date when this campaign will start', null=True, verbose_name='Start Date', blank=True),
        ),
        migrations.AddField(
            model_name='referrer',
            name='campaign_only',
            field=models.BooleanField(default=False, help_text='Should this referrer only count if it has a campaign?', verbose_name='Campaign Only'),
        ),
        migrations.AddField(
            model_name='referrer',
            name='display_name',
            field=models.CharField(help_text='This is an optional second name, useful for things like displaying', max_length=255, null=True, verbose_name='Display Name', blank=True),
        ),
    ]
