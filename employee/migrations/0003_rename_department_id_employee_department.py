# Generated by Django 4.1.1 on 2022-09-12 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_department_employee_department_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department_id',
            new_name='department',
        ),
    ]
