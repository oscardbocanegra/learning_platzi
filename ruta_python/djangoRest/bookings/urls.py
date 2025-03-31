from django.urls import path

from .views import (
    ListAppointmentView,
    DetailAppointmentView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
)


from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('appointments/<int:id>/', DetailAppointmentView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view()),
] + router.urls