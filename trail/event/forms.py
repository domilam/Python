from django import forms
from captcha.fields import ReCaptchaField

from event.models import Organizer, Event


class CommentForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['organizer', 'manager', 'tel', 'mail', 'website', 'logo']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event', 'startdate', 'enddate', 'organizer', 'description', 'email', 'website', 'affiche']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Objet')
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label='Votre email')
    cc_myself = forms.BooleanField(required=False, label="Envoi d'une copie")
    captcha = ReCaptchaField()

