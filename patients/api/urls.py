from rest_framework.routers import SimpleRouter
from patients.api import views
router = SimpleRouter()

router.register('patient', views.PatientViewSet)
urlpatterns = router.urls
