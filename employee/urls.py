from django.urls import path, include
from . import views
# from .views import EmployeeView


app_name = 'employee'

urlpatterns = [
    path('', views.create_get_employee, name='create'),
    path("id/<int:pk>/", views.get_update_delete_employee, name='get'),

]
