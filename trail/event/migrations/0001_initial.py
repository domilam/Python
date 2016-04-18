# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('event', models.CharField(max_length=70)),
                ('startdate', models.DateField(verbose_name='Date de début')),
                ('enddate', models.DateField(verbose_name='Date de fin')),
                ('description', models.TextField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name="email de l'evenement")),
                ('website', models.CharField(null=True, blank=True, max_length=150)),
                ('affiche', models.ImageField(null=True, blank=True, upload_to='event/event')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date_inscription', models.DateTimeField(auto_now_add=True, verbose_name="date de l'inscription")),
                ('licence_certif', models.FileField(upload_to='event/certif', null=True, blank=True, verbose_name='licence ou certificat médical ')),
                ('licence_number', models.CharField(null=True, blank=True, verbose_name='numéro de licence', max_length=35)),
                ('club', models.CharField(null=True, blank=True, max_length=40)),
                ('dossard', models.IntegerField(null=True, blank=True)),
                ('valide', models.BooleanField(default=False)),
                ('paye', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('organizer', models.CharField(max_length=50, verbose_name='organisateur')),
                ('manager', models.CharField(max_length=50, verbose_name='responsable')),
                ('tel', models.CharField(null=True, blank=True, verbose_name='téléphone', max_length=10)),
                ('mail', models.EmailField(max_length=70)),
                ('website', models.CharField(null=True, blank=True, max_length=150)),
                ('logo', models.ImageField(null=True, blank=True, upload_to='event/logo_organizer')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('race', models.CharField(max_length=70)),
                ('date_race', models.DateTimeField(verbose_name='date de la course')),
                ('distance', models.IntegerField()),
                ('unit', models.CharField(max_length=2, default='Kilomètres', choices=[('Km', 'Kilomètres'), ('mi', 'Miles')], verbose_name='unité')),
                ('height_difference', models.IntegerField(null=True, blank=True, verbose_name='dénivelé')),
                ('affiche', models.ImageField(null=True, blank=True, upload_to='event/race')),
                ('max_runner', models.IntegerField(null=True, blank=True, verbose_name='Nbre de coureur max')),
                ('event', models.ForeignKey(to='event.Event', verbose_name='évènement')),
            ],
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('last_name', models.CharField(max_length=50, verbose_name='nom du coureur')),
                ('first_name', models.CharField(max_length=50, verbose_name='prénom du coureur')),
                ('sex', models.CharField(max_length=1, default='M', choices=[('M', 'Masculin'), ('F', 'Féminin')], verbose_name='sexe')),
                ('birth_date', models.DateField(null=True, blank=True, verbose_name='date de naissance')),
                ('phone', models.CharField(null=True, blank=True, verbose_name='téléphone du coureur', max_length=15)),
                ('adress', models.TextField(null=True, blank=True, verbose_name='adresse')),
                ('zipcode', models.CharField(null=True, blank=True, verbose_name='code postal', max_length=5)),
                ('city', models.CharField(null=True, blank=True, verbose_name='ville', max_length=60)),
                ('identity_picture', models.ImageField(upload_to='event/identity', null=True, blank=True, verbose_name='photo')),
                ('first_contact', models.CharField(null=True, blank=True, verbose_name='contact à prevenir', max_length=100)),
                ('contact_phone', models.CharField(null=True, blank=True, verbose_name='téléphone contact', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Finisher',
            fields=[
                ('inscription', models.OneToOneField(serialize=False, to='event.Inscription', primary_key=True)),
                ('result', models.TimeField(verbose_name='temps')),
                ('category', models.CharField(null=True, blank=True, max_length=3)),
                ('rank', models.IntegerField(null=True, blank=True, verbose_name='classement')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='runner',
            field=models.ManyToManyField(to='event.Runner', through='event.Inscription'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='race',
            field=models.ForeignKey(to='event.Race'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='runner',
            field=models.ForeignKey(to='event.Runner'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(to='event.Organizer', verbose_name='organisateur'),
        ),
    ]
