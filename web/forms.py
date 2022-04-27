from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Your Name",'id':"name",'class':"form-control border-0 bg-light px-4"}),
            'phone':TextInput(attrs={'placeholder':"Your Phone",'id':"phone",'class':"form-control border-0 bg-light px-4"}),
            'email':EmailInput(attrs={'placeholder':"Your Email",'id':"email",'class':"form-control border-0 bg-light px-4"}),
            'message':Textarea(attrs={'placeholder':"Message",'id':"message",'class':"form-control border-0 bg-light px-4",'rows':"4"}),
         }