from rest_framework import routers
from .api import AnteikuViewSet

router = routers.DefaultRouter()
router.register('api/anteiku', AnteikuViewSet, 'anteiku')
urlpatterns = router.urls