from django.contrib import admin
from .models import Department, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('title', 'department', 'level')

admin.site.register(Department)
