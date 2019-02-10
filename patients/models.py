from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()
class Patient(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    cart_code = models.CharField(max_length=30)

    # Relationship Fields
    user = models.OneToOneField(User,related_name="patient", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.user.username

    def get_absolute_url(self):
        return reverse('patient_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('patient_update', args=(self.pk,))