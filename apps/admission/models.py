from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from apps.departement.models import Department


class Registration(models.Model):
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    date_of_birth = models.DateField()
    nationality = CountryField()
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True)
    id_number = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_email = models.EmailField(max_length=100, blank=True, null=True)
    guardian_address = models.CharField(max_length=100, blank=True, null=True)
    school_origin = models.CharField(max_length=100, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    student_card = models.CharField(max_length=200, editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='registrations')

    class Meta:
        unique_together = ('email', 'student_card')

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

@receiver(pre_save, sender=Registration)
def generate_student_card(sender, instance, *args, **kwargs):
    prefix = '0000'
    if Registration.objects.last():
        instance.student_card = prefix + str(Registration.objects.last().id + 1)
    else:
        instance.student_card = prefix + '1'
