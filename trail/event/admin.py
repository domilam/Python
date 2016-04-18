from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from event.models import *

# Register your models here.
AdminSite.site_url = '/event'
admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Race)
admin.site.register(Runner)
admin.site.register(Inscription)
admin.site.register(Finisher)
