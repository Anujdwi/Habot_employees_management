from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employees'),
    path('employees/<int:id>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-detail'),
]
