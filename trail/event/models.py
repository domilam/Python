from django.db import models


# Create your models here.

class Organizer(models.Model):
    organizer = models.CharField(max_length=50, verbose_name='organisateur')
    manager = models.CharField(max_length=50, verbose_name='responsable')
    tel = models.CharField(max_length=10, null=True, blank=True, verbose_name='téléphone')
    mail = models.EmailField(max_length=70)
    website = models.CharField(null=True, blank=True, max_length=150)
    logo = models.ImageField(null=True, blank=True, upload_to='event/logo_organizer')

    def __str__(self):
        return self.organizer


class Event(models.Model):
    event = models.CharField(max_length=70, verbose_name="nom de l'évènement")
    startdate = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Date de début")
    enddate = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Date de fin")
    organizer = models.ForeignKey(Organizer, verbose_name='organisateur')
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(verbose_name="email de l'évènement")
    website = models.CharField(null=True, blank=True, max_length=150, verbose_name='site web')
    affiche = models.ImageField(null=True, blank=True, upload_to='event/event')

    def __str__(self):
        return self.event


class Runner(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='nom du coureur')
    first_name = models.CharField(max_length=50, verbose_name='prénom du coureur')
    sex = models.CharField(max_length=1, choices=(('M', 'Masculin'), ('F', 'Féminin')),default='M', verbose_name='sexe')
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='date de naissance')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='téléphone du coureur')
    adress = models.TextField(null=True, blank=True, verbose_name='adresse')
    zipcode = models.CharField(max_length=5, null=True, blank=True, verbose_name='code postal')
    city = models.CharField(max_length=60, null=True, blank=True, verbose_name='ville')
    identity_picture = models.ImageField(null=True, blank=True, upload_to="event/identity", verbose_name='photo')
    first_contact = models.CharField(max_length=100, null=True, blank=True, verbose_name='contact à prevenir')
    contact_phone = models.CharField(max_length=10, null=True, blank=True, verbose_name='téléphone contact')

    def __str__(self):
        return '{0} - {1}'.format(self.first_name, self.last_name)


class Race(models.Model):
    race = models.CharField(max_length=70)
    date_race = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='date de la course')
    distance = models.IntegerField()
    unit = models.CharField(max_length=2, verbose_name='unité', choices=(('Km', 'Kilomètres'), ('mi', 'Miles')),
                            default='Kilomètres')
    height_difference = models.IntegerField(verbose_name='dénivelé', null=True, blank=True)
    affiche = models.ImageField(null=True, blank=True, upload_to="event/race")
    max_runner = models.IntegerField(verbose_name='Nbre de coureur max', null=True, blank=True)
    event = models.ForeignKey(Event, verbose_name='évènement')
    runner = models.ManyToManyField(Runner, through='Inscription')

    def __str__(self):
        return self.race


class Inscription(models.Model):
    date_inscription = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="date de l'inscription")
    runner = models.ForeignKey(Runner)
    race = models.ForeignKey(Race)
    licence_certif = models.FileField(null=True, blank=True, upload_to='event/certif',
                                      verbose_name='licence ou certificat médical ')
    licence_number = models.CharField(max_length=35, null=True, blank=True, verbose_name='numéro de licence')
    club = models.CharField(max_length=40, null=True, blank=True)
    dossard = models.IntegerField(null=True, blank=True)
    valide = models.BooleanField(default=False)
    paye = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.date_inscription, self.runner.first_name, self.runner.last_name)


class Finisher(models.Model):
    inscription = models.OneToOneField(Inscription, primary_key=True)
    result = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='temps')
    category = models.CharField(max_length=3, null=True, blank=True)
    rank = models.IntegerField(verbose_name='classement', null=True, blank=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.first_name, self.last_name, self.result)

