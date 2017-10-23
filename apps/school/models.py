from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=50)
    school_abreviation = models.CharField(max_length=10)
    school_slogan = models.CharField(max_length=50)
    adresse_line1 = models.CharField(max_length=50)
    adresse_line2 = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    autorization = models.CharField(max_length=10)
    registry_number = models.CharField(max_length=10)


    # class Meta:
    #     unique_together = ('email')

    def __str__(self):
        return '{0} {1}'.format(self.school_name, self.school_abreviation)
