from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    @action(["POST"], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "doctor is on vacation"})
    
    @action(["POST"], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "doctor is not on vacation"})