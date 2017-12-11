from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse #Used to generate urls by reversing the URL patterns
from django.contrib.auth.models import User

from django_countries.fields import CountryField

from apps.departement.models import Department, Course, CourseLevel
from apps.school.models import ActiveAcademicYear
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
        ('mathématique', 'Mathématiques'),
        ('experimentale', 'Experimentales'),
        ('sociale', 'Sociales'),
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
    id_card_number = models.CharField(max_length=50, blank=True, null=True)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_email = models.EmailField(max_length=100, blank=True, null=True)
    guardian_address = models.CharField(max_length=100, blank=True, null=True)
    school_origin = models.CharField(max_length=100, blank=True, null=True)
    option = models.CharField(max_length=32, choices=OPTION_CHOICE)
    year_admission_bac = models.CharField(max_length=4, blank=True, null=True)
    pv = models.CharField(max_length=10, blank=True, null=True)
    registration_add_date = models.DateTimeField(auto_now_add=True)
    registration_modify_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='student_images', default='avatar.png', blank=True, null=True)
    active_year = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_level = models.ForeignKey(CourseLevel, on_delete=models.CASCADE)
    # student_card=models.CharField(max_length=30, editable=False, blank=True, null=True)


    class Meta:
        ordering = ['pk']
        unique_together = ('email', 'registry_number')
        permissions = (("can_view_content", "Can see the specified content"),)

    def get_absolute_url(self):
        """
        Returns the url to access a particular registration instance.
        """
        return reverse('registration-detail', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit-registration', args=[str(self.id)])

    def get_registration_process_url(self):
        return reverse('new-process', args=[str(self.id)])

    def get_inscription_url(self):
        return reverse('new-inscription', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


#Generation a unique and autoincrement Matricule number for Student
def student_number():
    current_year = datetime.date.today().year
    prefix = "Mat-%d-%07d"
    try:
        last_student = Inscription.objects.last()
    except Admission.DoesNotExist:
        last_student = None

    if not last_student:
        return(prefix % (current_year, 1))
    else:
        last_id = last_student.id
        current_id = int(last_id) + 1
        return(prefix % (current_year, current_id))


#Define Admission process, it is a prerequisite before being accepted into the universtity
class AdmissionProcess(models.Model):

    registree = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name="process_registree")
    registree_number = models.CharField(max_length=50)
    registree_name = models.CharField(max_length=50)
    pass_bac = models.BooleanField()
    pass_admission_test = models.BooleanField()
    pass_medical_test = models.BooleanField()
    comment = models.TextField(max_length=1000, null=True, blank=True)
    commitee_decision = models.CharField(max_length=30)
    add_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular registration instance.
    #     """
    #     return reverse('admission-detail', args=[str(self.id)])

    def __str__(self):
        return(self.registree.registry_number)


#Define Inscription model
class Inscription(models.Model):
    registry = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name="reg_inscription")
    matricule = models.CharField(max_length=18, default=student_number, unique=True, editable=False)
    admission_add_date = models.DateTimeField(auto_now_add=True)
    admission_modify_date = models.DateTimeField(auto_now=True)
    active_year = models.ForeignKey(ActiveAcademicYear, max_length=32, on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    def get_absolute_url(self):
        """
        Returns the url to access a particular registration instance.
        """
        return reverse('admission-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.registry)

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
