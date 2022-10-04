from .models import Employee
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from employee.serializers import EmployeeSerializer, DepartmentSerializer


# Create your views here.


@api_view(['POST', 'GET'])
def create_get_employee(request):
    if request.method == 'POST':
        serialized_employee = EmployeeSerializer(data=request.data)
        if serialized_employee.is_valid():
            serialized_employee.save()
            return Response(serialized_employee.data, status=status.HTTP_201_CREATED)
        return Response("failed", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        queryset = Employee.objects.all()
        employee_serializer = EmployeeSerializer(queryset, many=True)
        return Response(employee_serializer.data)


@api_view(['GET', 'DELETE', 'PATCH'])
def get_update_delete_employee(request, pk):
    # Employee.objects.filter(first_name="name", age=23)
    # Employee.objects.filter(first_name__contains="sks")
    # return Employee.objects.all()[idd-1]
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response("employee does not exist", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized_employee = EmployeeSerializer(employee)
        return Response(serialized_employee.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        employee.delete()
        return Response("Deleted")

    elif request.method == 'PATCH':
        serialized_employee_details = JSONParser().parse(request)
        serialized_employee = EmployeeSerializer(employee, data=serialized_employee_details)
        if serialized_employee.is_valid():
            serialized_employee.save()
            return Response(serialized_employee.data, status=status.HTTP_202_ACCEPTED)

        return Response(serialized_employee.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_get_department(request):
    if request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return Response(department_serializer.data, status=status.HTTP_201_CREATED)
        return Response(department_serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
