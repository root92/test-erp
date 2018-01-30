from django import forms

from .models import Payement, Fees


class PayementForm(forms.ModelForm):

    class Meta:
        model = Payement
        fields =['fees', 'student', 'amount']
        labels = {
            'student': 'Elève',
            'fees': 'frais',
            'amount': 'Montant'
        }
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control form-element' }),
            'fees': forms.Select(attrs={'class': 'form-control form-element' }),
            'amount': forms.TextInput(attrs={'class': 'form-control form-element' }),
        }


class FeeForm(forms.ModelForm):

    class Meta:
        model = Fees 
        fields = ['label', 'fee_value', 'fee_description']
        labels = {
            'label': 'Libellé',
            'fee_value': 'Montant',
            'fee_description': 'Description',
        }
        widgets = {
            'label': forms.TextInput(attrs={'class': 'form-control form-element' }),
            'fee_value': forms.TextInput(attrs={'class': 'form-control form-element' }),
            'fee_description':forms.Textarea(attrs={'class': 'form-control admis-process-comment', 
                                    'required':False})
        }
