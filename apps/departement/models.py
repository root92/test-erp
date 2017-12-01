import uuid
from django.db import models
from apps.school.models import School

class Department(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=200, default='Computer Science',
                            unique=True)
    description = models.TextField(default='The best department')
    admission_fees = models.IntegerField()
    fees = models.IntegerField()
    # school = models.ForeignKey(School, on_delete=models.CASCADE)
    department_add_date = models.DateTimeField(auto_now_add=True)
    department_modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICE = (
        ('Licence', (
                ('l1', 'Licence 1'),
                ('l2', 'Licence 2'),
                ('l3', 'Licence 3'),
            )),
        ('Masters', (
                ('m1', 'Masters 1'),
                ('m2', 'Masters 2'),
            )),
    )
    title = models.CharField(max_length=200, default='Hacking', unique=True)
    level = models.CharField(max_length=7, choices=LEVEL_CHOICE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='courses')
    description = models.TextField(default='This Course is Awesome')
    course_add_date = models.DateTimeField(auto_now_add=True)
    course_modify_date = models.DateTimeField(auto_now=True)
    # _add_date = models.DateTimeField(auto_now_add=True)
    # _modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ClassRoom(models.Model):
    cr_code = models.CharField(max_length=6, verbose_name='Code')
    cr_label = models.CharField(max_length=30, verbose_name='Nom de la classe')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Departement')
    classroom_add_date = models.DateTimeField(auto_now_add=True)
    classroom_modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cr_label
