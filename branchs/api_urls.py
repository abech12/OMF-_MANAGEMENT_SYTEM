from rest_framework.routers import DefaultRouter
from .api_views import BranchOfficeViewSet

router = DefaultRouter()
router.register(r'branches', BranchOfficeViewSet)

urlpatterns = router.urls