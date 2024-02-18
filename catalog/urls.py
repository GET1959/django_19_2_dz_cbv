from django.urls import path

from catalog.views import HomeView, ContactsView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]