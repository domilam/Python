from django.db import models

# Create your models here.

class Auteur(models.Model):
    pseudo = models.CharField(max_length=25)
    Avatar = models.FileField(null=True, blank=True, upload_to="avatars/")
    nom = models.CharField(max_length=35)
    prenom = models.CharField(max_length=25)
    email = models.EmailField(max_length=70)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'inscription")

    def __str__(self):
        return self.pseudo

class MessageClassic(models.Model):
    date_message = models.DateTimeField(auto_now_add=True, verbose_name="Date du message")
    contenu_message = models.TextField(null=True, verbose_name="Contenu du message")
    auteur_message = models.ForeignKey(Auteur, verbose_name="Auteur du message")

    def __str__(self):
        return self.contenu_message

    def commentaires(self):
        """Cette méthode récupère tous les commentaires sur ce message
        """
        return self.commentaire_set.all()

    def recup_message_membre(self):
        """Cette méthode permettra de récupérer le destinataire des messages dans MessageMembre s'il existe
           s'il existe cela veut dire que le message a été posté par un autre membre sur mon mur
        """
        if hasattr(self, 'messagemembre'):#on vérifie que l'attribut existe
            return self.messagemembre.destinataire_message
        return None


class MessageMembre(MessageClassic):# hérite de MessageClassic et a un attribut en plus
    destinataire_message = models.ForeignKey(Auteur, verbose_name="Destinataire du message")


class Commentaire(models.Model):
    date_commentaire = models.DateTimeField(auto_now_add=True)
    contenu_commentaire = models.TextField(null=True)
    auteur_commentaire = models.ForeignKey(Auteur)
    message = models.ForeignKey(MessageClassic)

    class Meta:
        ordering = ['-date_commentaire'] #trie les commentaires par date décroissante

    def __str__(self):
        return self.contenu_commentaire
