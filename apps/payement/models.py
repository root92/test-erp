from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Used to generate urls by reversing the URL patterns

from apps.admission.models import AdmissionProcess

# Fees model
class Fees(models.Model):
    label = models.CharField(max_length=100)
    fee_value = models.DecimalField(max_digits=32, decimal_places=2)
    fee_description = models.CharField(max_length=250, null=True, blank=True)

    def get_edit_url(self):
        """
        Returns the url to access a particular fee instance.
        """
        return reverse('fee-edit', args=[str(self.id)])

    def get_delete_url(self):
        """
        Returns the url to access a particular fee instance.
        """
        return reverse('fee-delete', args=[str(self.id)])

    def __str__(self):
        return (self.label)


# Define Payement model
class Payement(models.Model):
    payement_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fees = models.ForeignKey(Fees, on_delete=models.CASCADE)
    student = models.ForeignKey(AdmissionProcess, on_delete=models.CASCADE,
                                related_name='registration_payement')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.fees.label, self.student.registree.first_name)
    