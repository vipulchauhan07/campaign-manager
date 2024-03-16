from rest_framework import viewsets
from .models import Campaign, TargetAudience, Owner, CampaignOwner
from .serializers import CampaignSerializer, TargetAudienceSerializer, OwnerSerializer, CampaignOwnerSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class TargetAudienceViewSet(viewsets.ModelViewSet):
    queryset = TargetAudience.objects.all()
    serializer_class = TargetAudienceSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class CampaignOwnerViewSet(viewsets.ModelViewSet):
    queryset = CampaignOwner.objects.all()
    serializer_class = CampaignOwnerSerializer
