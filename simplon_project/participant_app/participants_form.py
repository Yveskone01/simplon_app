from django import forms

from .models import Participants


class Participants_form(forms.Form):
    firstname = forms.CharField(max_length=250, required=True, label='Votre nom')
    lastname = forms.CharField(max_length=250, required=True, label='Votre prénom')
    phone = forms.EmailField(label='Votre email', required='True')

    def clean_firstname(self):
        firstname = self.cleaned_data.get('firstname')
        if len(firstname) < 1:
            raise forms.ValidationError('Veuillez entrer un nom valide')
        else:
            return firstname


class Form_Participation(forms.ModelForm):
    class Meta:
        model = Participants
        fields = '__all__'
