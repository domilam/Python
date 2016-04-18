from django.conf.urls import url, patterns

urlpatterns = patterns('social.views',
       url(r'^$', 'accueil', name='accueil'),
       url(r'^(?P<pseudo>\w+)$', 'profil', name='profil'),
                )



