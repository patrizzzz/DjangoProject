from rest_framework.routers import DefaultRouter
from .views import RecurringConfigViewSet


router = DefaultRouter()
router.register('recurringtransacconfig', RecurringConfigViewSet)
urlpatterns = router.urls