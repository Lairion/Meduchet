from django.contrib import admin
from .models import Patient
from .forms import PatientAdminForm
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    list_display = ['user','created', 'last_updated', 'cart_code']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Patient, PatientAdmin)
