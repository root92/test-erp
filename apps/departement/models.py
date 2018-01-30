from django.db import models


class ClassLevel(models.Model):
    label = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return (self.label)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE,
                                    verbose_name='class_subject')

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    code = models.CharField(max_length=6, verbose_name='Code')
    label = models.CharField(max_length=30, verbose_name='Nom de la classe')
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE,
                                    verbose_name='class_rooms')

    def __str__(self):
        return self.label
