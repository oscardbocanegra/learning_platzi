from rest_framework import viewsets, permissions

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    