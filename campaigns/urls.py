from django.urls import path, include
from rest_framework.routers import DefaultRouter
from campaigns.views import CampaignViewSet, TargetAudienceViewSet, OwnerViewSet, CampaignOwnerViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'targetaudience', TargetAudienceViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'campaignowners', CampaignOwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
