from django.shortcuts import render
from .models import ContactInfo
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContaktForm
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.base import TemplateView



class ContactView(FormView):
    template_name = 'contact_app/contact.html'
    form_class = ContaktForm
    success_url = reverse_lazy('contact_app:contact_erfolg_page')

    def form_valid(self, form):

        user_email = form.cleaned_data['user_email']
        betreff = form.cleaned_data['betreff']
        name = form.cleaned_data['name']
        nachricht = form.cleaned_data['nachricht']
        subject = 'Ihr habt eine neue Nachricht!'
        message = 'Ihr habt eine neue Nachricht'
        msg_html = render_to_string('contact_app/emails/email_contact.html', {'user_email':user_email,
                                                                                'name':name,
                                                                                'betreff':betreff,
                                                                                'nachricht':nachricht,})

        eigene_mail_adresse = settings.DEFAULT_FROM_EMAIL
        to_list = [eigene_mail_adresse,]

        send_mail(subject=subject,message=message, from_email=eigene_mail_adresse, recipient_list=to_list,html_message=msg_html,)



        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['auf_welcher_seite'] = 'contact'
        return context

class ContactViewErfolg(TemplateView):
    template_name = 'contact_app/contact_erfolg.html'
