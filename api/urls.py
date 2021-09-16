from django.urls import path
from rest_framework import routers

from api.views import ActivityViewSet

router = routers.SimpleRouter()
router.register('activity', ActivityViewSet)
urlpatterns = router.urls

