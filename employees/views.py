from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')

        if department:
            queryset = queryset.filter(department__iexact=department)
        if role:
            queryset = queryset.filter(role__iexact=role)

        return queryset


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def perform_update(self, serializer):
        email = serializer.validated_data.get('email')
        if email:
            if Employee.objects.exclude(id=self.get_object().id).filter(email=email).exists():
                raise ValidationError({"email": "Employee with this email already exists."})
        serializer.save()

    def delete(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)





# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Employee
# from .serializers import EmployeeSerializer


# class EmployeeCreateView(generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class EmployeeListView(generics.ListAPIView):
#     serializer_class = EmployeeSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         queryset = Employee.objects.all()
#         department = self.request.query_params.get('department')
#         role = self.request.query_params.get('role')

#         if department:
#             queryset = queryset.filter(department__iexact=department)
#         if role:
#             queryset = queryset.filter(role__iexact=role)

#         return queryset.order_by('id')


# class EmployeeDetailView(generics.RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'


# class EmployeeUpdateView(generics.UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'

#     def perform_update(self, serializer):
#         email = serializer.validated_data.get('email')
#         if email:
#             if Employee.objects.exclude(id=self.get_object().id).filter(email=email).exists():
#                 from rest_framework.exceptions import ValidationError
#                 raise ValidationError({"email": "Employee with this email already exists."})
#         serializer.save()


# class EmployeeDeleteView(generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'

#     def delete(self, request, *args, **kwargs):
#         self.perform_destroy(self.get_object())
#         return Response(status=status.HTTP_204_NO_CONTENT)
