from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import UserSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = ['name', 'email', 'description', 'data_agreement']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя','class': 'form_reg'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com','class': 'form_reg'}),
            'description': forms.Textarea(attrs={'placeholder': 'Ваше сообщение...', 'rows': 3,'class': 'form_reg'}),
        }
        labels = {
            'data_agreement': '✔️ Я согласен на обработку данных',
        }       
    