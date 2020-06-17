# sendemail/forms.py
from django import forms
from techguy.models import *
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_email(self):
        pass

class TechguyForm(forms.ModelForm):
    class Meta:
        model=Techguy
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = "__all__"

class OrderRequestForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']