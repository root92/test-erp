from django.contrib import admin
from .models import School, AcademicYear, ActiveAcademicYear

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = ('school_name', 'school_abreviation', 'school_slogan', 'school_add_date')

admin.site.register(AcademicYear)
admin.site.register(ActiveAcademicYear)