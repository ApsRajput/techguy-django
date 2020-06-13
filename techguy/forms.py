# sendemail/forms.py
from django import forms
from techguy.models import *

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class TechguyForm(forms.ModelForm):
    class Meta:
        model=Techguy
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"