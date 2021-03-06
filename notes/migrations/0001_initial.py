# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_type', models.CharField(max_length=20)),
                ('sub_category', models.CharField(max_length=20)),
                ('info_title', models.CharField(max_length=200)),
                ('info_text', models.CharField(max_length=100000)),
                ('pic_file', models.FileField(upload_to='')),
                ('comment', models.CharField(max_length=100000)),
            ],
        ),
    ]
