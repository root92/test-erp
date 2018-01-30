from django.contrib import admin

from .models import Inscription, Student


# Register your models here.
admin.site.register(Student)


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('registree', 'inscription_add_date')
    list_filter = ('registree', 'inscription_add_date')
    date_hierarchy = 'inscription_add_date'
    # ordering = ('inscription_add_date')
    search_fields = ('registree', 'active_year')

