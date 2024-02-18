from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from catalog.forms import ContactForm


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactsView(FormView):
    template_name = "catalog/contacts.html"
    form_class = ContactForm
    success_url = 'catalog/'
