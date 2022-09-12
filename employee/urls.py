from django.urls import path, include
from . import views
# from .views import EmployeeView



# router = routers.DefaultRouter
# router.register("e", EmployeeView, "create")
urlpatterns = [
    # path('create/', include(router.urls), 'create'),
    path('create/', views.create_employee, name='create'),
    # path('create/', EmployeeView.as_view()),
    path('delete/<num>/', views.get_employee_by_id),
    path('getAll/', views.get_all_employee),
    path('createDepartment/', views.create_department),
    path("id/<int:pk>/", views.get_employee_by_id)
]
