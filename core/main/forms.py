from django import forms
from .models import ContactPost

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = ContactPost
        fields = ['user_name', 'user_email', 'user_phone', 'user_message']