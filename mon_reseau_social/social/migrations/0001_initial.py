# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=25)),
                ('Avatar', models.FileField(null=True, upload_to='avatars/', blank=True)),
                ('nom', models.CharField(max_length=35)),
                ('prenom', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=70)),
                ('date', models.DateTimeField(verbose_name="Date d'inscription", auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commentaire', models.DateTimeField(auto_now_add=True)),
                ('contenu_commentaire', models.TextField(null=True)),
                ('auteur_commentaire', models.ForeignKey(to='social.Auteur')),
            ],
        ),
        migrations.CreateModel(
            name='MessageClassic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_message', models.DateTimeField(verbose_name='Date du message', auto_now_add=True)),
                ('contenu_message', models.TextField(null=True, verbose_name='Contenu du message')),
            ],
        ),
        migrations.CreateModel(
            name='MessageMembre',
            fields=[
                ('messageclassic_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='social.MessageClassic')),
                ('destinataire_message', models.ForeignKey(verbose_name='Destinataire du message', to='social.Auteur')),
            ],
            bases=('social.messageclassic',),
        ),
        migrations.AddField(
            model_name='messageclassic',
            name='auteur_message',
            field=models.ForeignKey(verbose_name='Auteur du message', to='social.Auteur'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='message',
            field=models.ForeignKey(to='social.MessageClassic'),
        ),
    ]
