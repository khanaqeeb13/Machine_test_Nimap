from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('projects', ProjectViewSet, basename='projects')

urlpatterns = router.urls