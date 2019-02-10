from django.contrib import admin
from .forms import DoctorAdminForm
from .models import Doctor
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    form = DoctorAdminForm
    list_display = ['user','created', 'last_updated', 'access_cart']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Doctor, DoctorAdmin)