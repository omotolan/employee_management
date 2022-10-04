from django.db import models


# Create your models here.

class Department(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Qualification(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='Employees')


class Employee(models.Model):
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('NON_BINARY', 'Non Binary')
    )
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    is_suspended = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
