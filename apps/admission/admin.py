from django.contrib import admin
from .models import Registration, Admission, AdmissionProcess


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    list_display = ('registry_number', 'first_name', 'last_name', 'id_card_number', 'registration_add_date')
    list_filter = ('registry_number','registration_add_date', )
    date_hierarchy = 'registration_add_date'
    ordering = ('registration_add_date', )
    search_fields = ('registry_number', 'first_name')

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Information personnel', {
            'classes': ['collapse',],
            'description':u'Information personnel',
            'fields': ('first_name', 'last_name', 'gender', 'date_of_birth', 'nationality', 'address', 'phone_number', 'email', 'id_card_number')
        }),
        # Fieldset 2 : parti concernant la famille
        ('Information sur la famille ou le tuteur', {
            'description':u'Information sur la famille ou le tuteur',
            'fields': ('fathers_name', 'mothers_name', 'guardian_name', 'guardian_phone', 'guardian_email', 'guardian_address')
        }),
        # Fieldset 3 : l'ecole d'origin
        ('Parcours pre-universitaire', {
            'description':u'Parcours pre-universitaire',
            'fields': ('school_origin', 'option', 'year_admission_bac', 'pv')
        }),
    )

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):

    list_display = ('matricule', 'registry', 'academic_year', 'class_level', 'admission_add_date')
    list_filter = ('matricule','registry', 'admission_add_date' )
    date_hierarchy = 'admission_add_date'
    ordering = ('admission_add_date', )
    search_fields = ('matricule', 'registry')


admin.site.register(AdmissionProcess)