from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse #Used to generate urls by reversing the URL patterns

from django_countries.fields import CountryField

from apps.departement.models import Department, ClassRoom
from apps.school.models import AcademicYear
# from .number_generations import registration_number, student_number

import datetime

#Defining path to images
def get_image_path(instance, filename):
    return '/'.join(['student_images', str(instance.name), filename])


#Generation a unique and autoincrement Registation number
def registration_number():
    current_year = datetime.date.today().year
    prefix = "Reg-%d-%07d"
    try:
        last_reg = Registration.objects.last()
    except Registration.DoesNotExist:
        last_reg = None
    
    if not last_reg:
        return(prefix % (current_year, 1))
    else: 
        last_id = last_reg.id
        current_id = int(last_id) + 1
        return (prefix % (current_year, current_id))


#Define Registration model
class Registration(models.Model):
    GENDER_CHOICE = (
        ('homme', 'homme'),
        ('femme', 'femme'),
    )

    OPTION_CHOICE = (
        ('sm', 'Sciences Mathématiques'),
        ('se', 'Sciences Experimentales'),
        ('ss', 'Sciences Sociales'),
    )

    registry_number = models.CharField(max_length=18, default=registration_number, unique=True, editable=False)
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
    id_card_number = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_email = models.EmailField(max_length=100, blank=True, null=True)
    guardian_address = models.CharField(max_length=100, blank=True, null=True)
    school_origin = models.CharField(max_length=100, blank=True, null=True)
    option = models.CharField(max_length=2, choices=OPTION_CHOICE)
    year_admission_bac = models.CharField(max_length=4, blank=True, null=True)
    pv = models.CharField(max_length=10, blank=True, null=True)
    registration_add_date = models.DateTimeField(auto_now_add=True)
    registration_modify_date = models.DateTimeField(auto_now=True)
    student_card = models.CharField(max_length=200, editable=False)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='registrations')
    


    class Meta:
        ordering = ['-pk']
        unique_together = ('email', 'student_card')
        permissions = (("can_view_content", "Can see the specified content"),)

    def get_absolute_url(self):
        """
        Returns the url to access a particular registration instance.
        """
        return reverse('registration-detail', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit-registration', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


#Generation a unique and autoincrement Matricule number for Student
def student_number():
    current_year = datetime.date.today().year
    prefix = "Mat-%d-%07d"
    try:
        last_student = Admission.objects.last()
    except Admission.DoesNotExist:
        last_student = None
   
    if not last_student:
        return(prefix % (current_year, 1))
    else:
        last_id = last_student.id
        current_id = int(last_id) + 1
        return(prefix % (current_year, current_id))


#Define Admission model
class Admission(models.Model):
    registry = models.OneToOneField(Registration, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    class_level = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='admissions')
    image = models.ImageField(upload_to='student_images', default='avatar.png')
    # fees = models.IntegerField()
    matricule = models.CharField(max_length=18, default=student_number, unique=True, editable=False)
    admission_add_date = models.DateTimeField(auto_now_add=True)
    admission_modify_date = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular registration instance.
        """
        return reverse('admission-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.registry)


#Define Admission process, it is a prerequisite before being accepted into the universtity
class AdmissionProcess(models.Model):
    registree = models.ForeignKey(Registration, on_delete=models.CASCADE)
    payment_date = models.DateField()
    registration_fees_paid = models.DecimalField(max_digits=32, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='admission_process')

    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular registration instance.
    #     """
    #     return reverse('admission-detail', args=[str(self.id)])

    def __str__(self):
        return(self.registree.registry_number)




# @receiver(pre_save, sender=Registration)
# def generate_student_card(sender, instance, *args, **kwargs):
#     prefix = "Reg-%d-%07d"
#     current_year = datetime.date.today().year
#     last_reg = Registration.objects.last()
#     if not last_reg:
#         instance.registry_number = prefix % (current_year, 1)
#     else:
#         last_id = last_reg.id
#         current_id = int(last_id) + 1
#         instance.registry_number = prefix % (current_year, current_id)

# @receiver(pre_save, sender=Admission)
# def generate_student_matricule(sender, instance, *args, **kwargs):
#     prefix = "Mat-%d-%07d"
#     current_year = datetime.date.today().year
#     last_adm = Admission.objects.last()
#     if not last_adm:
#         instance.matricule = prefix % (current_year, 1)
#     else:
#         last_id = last_adm.id
#         current_id = int(last_id) + 1
#         instance.matricule = prefix % (current_year, current_id)


