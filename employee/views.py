from django.shortcuts import render
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from employee.serializers import EmployeeSerializer, DepartmentSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


# class EmployeeView(APIView):
    # def create(self, request):
    #     if request.method == 'POST':
    #         serialized_employee = EmployeeSerializer(data=request.data)
    #         if serialized_employee.is_valid():
    #             serialized_employee.save()
    #             return Response(serialized_employee.data, status=status.HTTP_201_CREATED)
    #         return Response("failed", status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        # employee_data = JSONParser().parse(request)
        serialized_employee = EmployeeSerializer(data=request.data)
        if serialized_employee.is_valid():
            serialized_employee.save()
            return Response(serialized_employee.data, status=status.HTTP_201_CREATED)
        return Response("failed", status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET'])
def get_employee_by_id(request, pk):
    # Employee.objects.filter(first_name="name", age=23)
    # Employee.objects.filter(first_name__contains="sks")
    # return Employee.objects.all()[idd-1]

    employee = find_employee_internal(pk)

    if request.method == 'GET':
        serialized_employee = EmployeeSerializer(employee)
        return Response(serialized_employee.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_employee_by_id(request, pk):
    if request.method == 'DELETE':
        try:
            employee = find_employee_internal(pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response("Deleted")


@api_view(['GET'])
def get_all_employee(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return Response(employee_serializer.data)


@api_view(['POST'])
def create_department(request):
    if request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return Response(department_serializer.data, status=status.HTTP_201_CREATED)
        return Response(department_serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_employee_details(request, pk):
    if request.method == 'PUT':
        serialized_employee_details = JSONParser().parse(request)
        employee = find_employee_internal(pk)
        serialized_employee = EmployeeSerializer(employee, data=serialized_employee_details)
        if serialized_employee.is_valid():
            serialized_employee.save()
            return Response(serialized_employee.data, status=status.HTTP_202_ACCEPTED)

        return Response(serialized_employee.error_messages, status=status.HTTP_400_BAD_REQUEST)


def find_employee_internal(pk):
    # try:
    employee = Employee.objects.get(id=pk)
    if employee == 'null':
        raise Exception("user does not exist")
    # except Employee.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    return employee


# class USERNODEY(Exception):


@csrf_exempt
def hello(request):
    if request.method == 'POST':
        return JsonResponse("hello", safe=False)
