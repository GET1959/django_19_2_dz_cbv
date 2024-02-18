from django import forms
from catalog.models import ContactData

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactData
        fields = ('name', 'phone', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'name': "name", 'placeholder': "Введите ваше имя"}),
            'phone': forms.TextInput(attrs={'class': "form-control", 'name': "phone", 'placeholder': "Введите ваш телефон"}),
            'message': forms.TextInput(attrs={'class': "form-control", 'name': "message", 'placeholder': "Введите сообщение"}),
        }