from rest_framework.routers import SimpleRouter
from doctors.api import views
router = SimpleRouter()

router.register('doctor', views.DoctorViewSet)
urlpatterns = router.urls
