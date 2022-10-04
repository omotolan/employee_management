from django.contrib import admin

from employee import models


# Register your models here.

# admin.site.register(models.Employee)
# admin.site.register(models.Department)


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_editable = ['is_suspended', 'department_name']
    list_per_page = 20

    def department_name(self, employee):
        return employee.department.name


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_editable = ['name']
