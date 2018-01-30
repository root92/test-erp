from django.contrib import admin
from .models import ClassLevel, Subject, ClassRoom


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_level')


@admin.register(ClassLevel)
class ClasslevelAdmin(admin.ModelAdmin):
    list_display = ('label', 'description')


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('code', 'label')
    # list_filter = ('cr_code', 'cr_label')
