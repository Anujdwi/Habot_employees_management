from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employees'),
    path('employees/<int:id>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-detail'),
]





# from django.urls import path
# from .views import (
#     EmployeeCreateView,
#     EmployeeListView,
#     EmployeeDetailView,
#     EmployeeUpdateView,
#     EmployeeDeleteView
# )

# urlpatterns = [
#     path('employees/', EmployeeCreateView.as_view(), name='create-employee'),
#     path('employees/', EmployeeListView.as_view(), name='list-employees'),
#     path('employees/<int:id>/', EmployeeDetailView.as_view(), name='get-employee'),
#     path('employees/<int:id>/', EmployeeUpdateView.as_view(), name='update-employee'),
#     path('employees/<int:id>/', EmployeeDeleteView.as_view(), name='delete-employee'),
# ]
