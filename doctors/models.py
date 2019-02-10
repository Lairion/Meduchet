from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Doctor(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    access_cart = models.CharField(max_length=30)

    # Relationship Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='doctor'
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.user.username

    def get_absolute_url(self):
        return reverse('doctor_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('doctor_update', args=(self.pk,))