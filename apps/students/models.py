from django.db import models
from apps.admission.models import Registration

# Create your models here.
# class students(models.Model):

# class Students(models.Model):
#     matricule
#     first_name
#     last_name
#     gender
#     date_of_admission
#     fees
#     academic_year


# class grades(models.Model):



# the payement of de students
class Payement(models.Model):
    registree = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='registration_payement')
    payment_type = models.CharField(max_length=64)
    date = models.DateField()
    amount = models.DecimalField(max_digits=32, decimal_places=2)

    def __str__(self):
        return '{0} {1}'.format(self.payment_type, self.registree.first_name)

