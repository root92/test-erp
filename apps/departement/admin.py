from django.contrib import admin
from .models import Department, Course, ClassRoom


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('title', 'department', 'level')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('cr_code', 'cr_label', 'department')
    # list_filter = ('cr_code', 'cr_label')


# admin.site.register(Department)
# admin.site.register(ClassRoom)


