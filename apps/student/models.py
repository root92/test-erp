from django.db import models
from django.contrib.auth.models import User

from apps.admission.models import AdmissionProcess
from apps.departement.models import ClassLevel
from apps.school.models import ActiveAcademicYear


class Student(models.Model):
    registree = models.OneToOneField(AdmissionProcess, on_delete=models.CASCADE,
                                    related_name='registration_student')

    def __str__(self):
        return (self.registree.reg_inscription.matricule)


# Define Inscription model
class Inscription(models.Model):
    registree = models.ForeignKey(AdmissionProcess, on_delete=models.CASCADE,
                                  related_name="reg_inscription")
    active_year = models.ForeignKey(ActiveAcademicYear, max_length=32, on_delete=models.CASCADE)
    class_level = models.ForeignKey(ClassLevel, max_length=32, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    inscription_add_date = models.DateTimeField(auto_now_add=True)
    inscription_modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.registree)

