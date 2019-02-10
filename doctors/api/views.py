from rest_framework import viewsets,mixins
from doctors.api.serializers import DoctorSerializer
from doctors.models import Doctor

class DoctorViewSet(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
