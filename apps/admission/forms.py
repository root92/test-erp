from django import forms

from .models import Registration, Admission

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        labels = {
            'first_name': 'Prenom',
            'last_name': 'Nom',
            'gender': 'Genre',
            'date_of_birth': 'Date de Naissance',
            'nationality': 'Nationalié',
            'fathers_name': 'Nom du père',
            'mothers_name': 'Nom de la mère',
            'address': 'Adresse',
            'phone_number': 'Numéro de Téléphone',
            'email': 'Email',
            'id_card_number': "Numéro Carte d'identité",
            'guardian_name': 'Nom du tuteur',
            'guardian_phone': 'Numero de éléphone du tuteur',
            'guardian_email': 'Email du tuteur',
            'guardian_address': 'Adresse du tuteur',
            'school_origin': "Ecole d'origine",
            'option': 'options',
            'year_admission_bac': "Année d'admission Baccalauréat",
            'pv': 'Pv'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-element' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-element' }),
            'gender': forms.Select(attrs={'class': 'form-control form-element'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control form-element'}),
            'nationality': forms.Select(attrs={'class': 'form-control form-element'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'id_card_number': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'guardian_email': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'guardian_address': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'school_origin': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'option': forms.Select(attrs={'class': 'form-control form-element'}),
            'year_admission_bac': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'pv': forms.TextInput(attrs={'class': 'form-control form-element'})
        }
        

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields ='__all__'

