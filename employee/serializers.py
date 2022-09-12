from rest_framework import serializers
from employee.models import Department, Employee, Qualification


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ('first_name', 'last_name', 'email', 'age', 'department_id',
        #           'gender', 'salary', 'is_suspended',
        #           'date_joined'
        #           )
# class PizzaSerializer(serializers.ModelSerializer):
#     order = OrderSummarySerializer(read_only=True)
#     box = BoxSerializer(read_only=True)
#     toppings = ToppingSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Pizza
#         fields = ('id', 'order', 'box', 'toppings')
