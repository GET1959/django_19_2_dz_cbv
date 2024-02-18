from django.db import models


class ContactData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=250)
