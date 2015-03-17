# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistributedFilesystem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_replication', models.IntegerField()),
                ('max_replication', models.IntegerField()),
                ('min_write_retries', models.IntegerField()),
                ('max_write_retries', models.IntegerField()),
                ('min_block_size', models.IntegerField()),
                ('max_block_size', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DistributedProgramming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_reduce_tasks', models.IntegerField()),
                ('max_reduce_tasks', models.IntegerField()),
                ('min_map_tasks', models.IntegerField()),
                ('max_map_tasks', models.IntegerField()),
                ('support_streaming', models.BooleanField()),
                ('programming_language', models.CharField(default='java', max_length=6, choices=[('python', 'PYTHON'), ('java', 'JAVA'), ('scala', 'SCALA'), ('all', 'ALL')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MachineLearning',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('open_source', models.BooleanField(default=False)),
                ('distributed', models.BooleanField(default=False)),
                ('supervise_learning', models.BooleanField(default=False)),
                ('unsupervise_learning', models.BooleanField(default=False)),
                ('reinforcement_learning', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SQLonHadoop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('execute_engine', models.CharField(default='mr', max_length=3, choices=[('tez', 'TEZ'), ('mr', 'MR'), ('all', 'ALL')])),
                ('min_tread_workers', models.IntegerField()),
                ('max_tread_workers', models.IntegerField()),
                ('allow_multiple_session', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
