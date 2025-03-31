from django.urls import path

from .views import ListPatientsView, DetailPatientView
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)

urlpatterns = [
    path('patients/', ListPatientsView.as_view()),
    path('patients/<int:pk>/', DetailPatientView.as_view()),
] + router.urls