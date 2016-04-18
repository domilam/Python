from django.shortcuts import render
from social.models import MessageClassic, Auteur
from django.views.decorators.cache import cache_page


# Create your views here.

def accueil(request):
    """
    Récupère la liste des profils pour l'accueil
    """
    list_auteur = Auteur.objects.all()
    return render(request, 'social/accueil.html', {'auteurs': list_auteur})

#@cache_page(60 * 1) je n'utilise pas le cache pour l'instant
def profil(request, pseudo):
    """
    récupère la liste des messages triés par ordre décroissant des dates de message
    """
    list_message = MessageClassic.objects.all().order_by('-date_message').select_related('messagemembre')
    return render(request, 'social/profil.html', locals())
