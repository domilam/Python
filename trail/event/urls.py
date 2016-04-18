from django.conf.urls import url, patterns


urlpatterns = patterns('event.views',
                       url(r'^$', 'agenda', name='accueil'),
                       url(r'^agenda$', 'agenda', name='agenda'),
                       url(r'^course$', 'course', name='course'),
                       url(r'^resultat$', 'resultat', name='resultat'),
                       url(r'^contact$', 'contact', name='contact'),
                       url(r'^addevent$', 'addevent', name='addevent'),
                       url(r'^thanks$', 'thanks', name='thanks'),
                       url(r'^listrunner/(?P<id_race>\d+)$', 'listrunner', name='listrunner'),
                       )
