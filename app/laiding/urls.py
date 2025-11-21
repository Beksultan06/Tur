from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SettingsViewSet, ValuesViewSet, ImageViewSet, DirectionViewSet,
    DirectionImageViewSet, PartnerImageViewSet, ReviewsViewSet,
    BlogViewSet, FeedbackViewSet, ServiseAPI, StatisticViewSet
)

router = DefaultRouter()
router.register(r'settings', SettingsViewSet)
router.register(r'values', ValuesViewSet)
router.register(r'images', ImageViewSet)
router.register(r'directions', DirectionViewSet)
router.register(r'direction-images', DirectionImageViewSet)
router.register(r'partners', PartnerImageViewSet)
router.register(r'reviews', ReviewsViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'services', ServiseAPI)
router.register(r'statistic', StatisticViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
