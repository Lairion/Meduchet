from rest_framework import serializers 
from patients.models import Patient

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
