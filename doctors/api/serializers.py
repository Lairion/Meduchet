from rest_framework import serializers 
from doctors.models import Doctor

class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
