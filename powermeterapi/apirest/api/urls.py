from django.urls import path, include
from rest_framework import routers

from .apiviews import MeasurerViewset, MeasurerHistoryViewset

router = routers.DefaultRouter()
router.register(r'measurer', MeasurerViewset, basename="measurer")
router.register(r'measurerhistory', MeasurerHistoryViewset, basename="measurerhistory")

urlpatterns = [
    path('', include(router.urls))
]