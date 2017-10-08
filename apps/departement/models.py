import uuid
from django.db import models


class Department(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    name = models.CharField(max_length=200, default='Computer Science',
                            unique=True)
    description = models.TextField(default='The best department')

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICE = (
        ('Licence', (
                ('l1', 'Licence 1'),
                ('l2', 'Licence 2'),
                ('l3', 'Licence 3'),
            )
        ),
        ('Masters', (
                ('m1', 'Masters 1'),
                ('m2', 'Masters 2'),
            )
        ),
    )
    code = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    title = models.CharField(max_length=200, default='Hacking', unique=True)
    level = models.CharField(max_length=7, choices=LEVEL_CHOICE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='courses')
    description = models.TextField(default='This Course is Awesome')

    def __str__(self):
        return self.title
