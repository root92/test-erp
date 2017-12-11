import uuid
from django.db import models
from apps.school.models import School

class Department(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=200,
                            unique=True)
    description = models.TextField(null=True, blank=True)
    admission_fees = models.IntegerField()
    # school = models.ForeignKey(School, on_delete=models.CASCADE)
    department_add_date = models.DateTimeField(auto_now_add=True)
    department_modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(max_length=200,  unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE , related_name='courses')
    description = models.TextField(null=True, blank=True)
    course_add_date = models.DateTimeField(auto_now_add=True)
    course_modify_date = models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.name

class CourseLevel(models.Model):
    LEVEL_CHOICE = (
        ('Licence', (
                ('lic1', 'Licence 1'),
                ('lic2', 'Licence 2'),
                ('lic3', 'Licence 3'),
            )),
        ('Masters', (
                ('mas1', 'Masters 1'),
                ('mas2', 'Masters 2'),
            )),
    )
    code_level = models.CharField(max_length=16)
    level = models.CharField(max_length=7, choices=LEVEL_CHOICE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.level

class ClassRoom(models.Model):
    cr_code = models.CharField(max_length=6, verbose_name='Code')
    cr_label = models.CharField(max_length=30, verbose_name='Nom de la classe')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Departement')
    classroom_add_date = models.DateTimeField(auto_now_add=True)
    classroom_modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cr_label
