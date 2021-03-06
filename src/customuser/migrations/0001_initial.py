# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 21:41
from __future__ import unicode_literals

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(help_text='Email Personal.', max_length=100, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(help_text='Personal Info.', max_length=150)),
                ('last_name', models.CharField(help_text='Personal Info.', max_length=150)),
                ('status', models.CharField(blank=True, choices=[('ACTIVATED', 'ACTIVATED'), ('DEACTIVATED', 'DEACTIVATED'), ('BANNED', 'BANNED'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED')], default='PENDING', help_text='User status', max_length=15, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'myuser',
                'ordering': ['-created'],
            },
        ),
    ]
