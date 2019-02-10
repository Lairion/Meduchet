from django import forms
from .models import Doctor

class DoctorAdminForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'

