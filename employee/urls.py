from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_employee),
    path('delete/<num>/', views.get_employee_by_id),
    path('getAll/', views.get_all_employee),
    path('createDepartment/', views.create_department),
    path("id/<int:pk>/", views.get_employee_by_id)
]
