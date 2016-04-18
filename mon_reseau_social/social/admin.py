from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from social.models import *

class AuteurAdmin(admin.ModelAdmin):
	list_display = ('pseudo', 'nom', 'prenom', 'email', 'date')
	list_filter = ('pseudo', )
	date_hierarchy = 'date'
	ordering = ('date', )
	search_fields = ('pseudo', )

class MessageClassicAdmin(admin.ModelAdmin):
	list_display = ('date_message', 'contenu_message', 'auteur_message')
	list_filter = ('auteur_message', )
	date_hierarchy = 'date_message'
	ordering = ('-date_message', )
	search_fields = ('auteur_message', )

class MessageMembreAdmin(admin.ModelAdmin):
	list_display = ('date_message', 'contenu_message', 'auteur_message', 'destinataire_message')
	list_filter = ('auteur_message', 'destinataire_message' )
	date_hierarchy = 'date_message'
	ordering = ('-date_message', )
	search_fields = ('auteur_message', )

class CommentaireAdmin(admin.ModelAdmin):
	list_display = ('date_commentaire', 'contenu_commentaire', 'auteur_commentaire', 'message')
	list_filter = ('auteur_commentaire', )
	date_hierarchy = 'date_commentaire'
	ordering = ('-date_commentaire', )
	search_fields = ('auteur_commentaire', )



# Register your models here.
AdminSite.site_url='/social'
admin.site.register(Auteur, AuteurAdmin)
admin.site.register(MessageClassic, MessageClassicAdmin)
admin.site.register(MessageMembre, MessageMembreAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
