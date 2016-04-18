from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render_to_response

from datetime import datetime
from django.utils import timezone

from event.models import Event, Race, Finisher, Inscription
from event.forms import EventForm, ContactForm


# Create your views here.
def agenda(request):
    liste_id = {0: "collapseOne", 1: "collapseTwo", 2: "collapseThree", 3: "collapseFor",
                4: "collapseFive", 5: "collapseSix", 6: "collapseSeven", 7: "collapseEigth"}
    events = Event.objects.filter(startdate__gte=datetime.now()).order_by('startdate')
    return render(request, 'event/agenda.html', {'events': events, 'liste_id': liste_id})


def course(request):
    races = Race.objects.filter(date_race__gte=timezone.now()).order_by('date_race')
    return render(request, 'event/course.html', locals())


def contact(request):
    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            m_subject = contactform.cleaned_data['subject']
            m_message = contactform.cleaned_data['message']
            m_sender = contactform.cleaned_data['sender']
            m_cc_myself = contactform.cleaned_data['cc_myself']
            m_recipients = ['contact@japplique.com']
            if m_cc_myself:
                m_recipients.append(m_sender)
            send_mail(m_subject, m_message, m_sender, m_recipients)
            return HttpResponseRedirect('thanks')
    else:
        contactform = ContactForm()
    return render(request, 'event/contact.html', locals())


def resultat(request):
    resultats = Finisher.objects.all()
    return render(request, 'event/resultat.html', locals())


def addevent(request):
    if request.method == 'POST':
        eventform = EventForm(request.POST)
        if eventform.is_valid():
            event = Event()
            event.event = eventform.cleaned_data['event']
            event.startdate = eventform.cleaned_data['startdate']
            event.enddate = eventform.cleaned_data['enddate']
            event.organizer = eventform.cleaned_data['organizer']
            event.description = eventform.cleaned_data['description']
            event.email = eventform.cleaned_data['email']
            event.website = eventform.cleaned_data['website']
            event.affiche = eventform.cleaned_data['affiche']
            event.save()
            return HttpResponseRedirect('agenda')

    else:
        eventform = EventForm()
    return render(request, 'event/addevent.html', locals())


def thanks(request):
    return render(request, 'event/thanks.html', locals())


def listrunner(request, id_race):
    listinscrit = Inscription.objects.filter(race=id_race)
    return render_to_response('event/listrunner.html', locals())
