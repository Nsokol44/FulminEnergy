from django import forms
from landing.models import Information
from django.core.exceptions import ObjectDoesNotExist

class SignUpForm(forms.ModelForm):
    questions = forms.CharField(required=False)
    class Meta():
        model = Information
        fields = ('firstName', 'lastName', 'email', 'questions')
        labels = {'firstName': 'First Name', 'lastName': 'Last Name', 'email': 'Email Address', 'questions': 'Questions'}

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()

        try:
            match = Information.objects.get(email = email.lower())
        except ObjectDoesNotExist:
            return email

        raise forms.ValidationError('You have already provided your information. We will contact you as soon as our product is ready. Thank you!')
