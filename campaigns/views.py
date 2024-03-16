from datetime import timedelta, timezone
from warnings import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Campaign, TargetAudience, Owner, CampaignOwner
from .serializers import CampaignSerializer, TargetAudienceSerializer, OwnerSerializer, CampaignOwnerSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
   

class TargetAudienceViewSet(viewsets.ModelViewSet):
    # queryset = TargetAudience.objects.all()
    # serializer_class = TargetAudienceSerializer
    queryset1 = TargetAudience.objects.all()
    serializer_class = TargetAudienceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['age', 'gender_type']
    ordering_fields = ['age']

    def get_queryset(self):
        queryset = super().get_queryset()
        age = self.request.query_params.get('age')
        gender_type = self.request.query_params.get('gender_type')
        if age:
            queryset = queryset.filter(age)
        if gender_type:
            queryset = queryset.filter(gender_type)

        return queryset

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class CampaignOwnerViewSet(viewsets.ModelViewSet):
    queryset = CampaignOwner.objects.all()
    serializer_class = CampaignOwnerSerializer
