from rest_framework import viewsets,mixins
from patients.api.serializers import PatientSerializer
from patients.models import Patient

class PatientViewSet(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
