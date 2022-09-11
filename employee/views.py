from django.shortcuts import render
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from employee.serializers import EmployeeSerializer, DepartmentSerializer
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("successful", safe=False)
        return JsonResponse("failed", safe=False, status=404)


@csrf_exempt
def get_employee_by_id(request, pk):
    # Employee.objects.filter(first_name="name", age=23)
    # Employee.objects.filter(first_name__contains="sks")
    # return Employee.objects.all()[idd-1]
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        employee = Employee.objects.get(id=pk)
        employee_serializer = EmployeeSerializer(employee)
        return JsonResponse(employee_serializer.data, safe=True)


def delete_employee_by_id(idd):
    employee = Employee.objects.all()[idd - 1]
    employee.delete()


@csrf_exempt
def get_all_employee(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)


@csrf_exempt
def create_department(request):
    if request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("successful", safe=False)
        return JsonResponse("failed", safe=False, status=404)


@csrf_exempt
def hello(request):
    if request.method == 'POST':
        return JsonResponse("hello", safe=False)
