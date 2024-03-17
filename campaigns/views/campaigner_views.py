from datetime import timedelta, timezone
from warnings import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response, status
from django.db.models import Q
from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer
from django.utils import timezone

@api_view(['POST', 'PUT'])
def createCampaign(request):
    data = request.data
    try:
        if request.method == 'POST':
            # For POST requests, create a new campaign
            campaign = Campaign.objects.create(
                name=data['name'],
                description=data['description'],
                country=data['country'],
                marketing_channel=data['marketing_channel'],
                is_active=data['active'],
                created_at=timezone.now()  # Set the created_at field automatically
            )
        elif request.method == 'PUT':
            # For PUT requests, update an existing campaign if it exists
            campaign_id = data.get('id')  # Assuming id is provided in the request data
            campaign = Campaign.objects.get(pk=campaign_id)
            campaign.name = data['name']
            campaign.description = data['description']
            campaign.country = data['country']
            campaign.marketing_channel = data['marketing_channel']
            campaign.is_active = data['active']
            campaign.updated_at = timezone.now()
            campaign.save()
        
        serializer = CampaignSerializer(campaign, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error occurred.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
   
   


@api_view(['GET'])
def getCampaign(request):
    try:
        # Retrieve query parameters from the request
        name = request.query_params.get('name', None)
        country = request.query_params.get('country', None)
        marketing_channel = request.query_params.get('marketing_channel', None)
        is_active = request.query_params.get('active', None)

        # Build filter conditions
        filter_conditions = Q()
        if name:
            filter_conditions &= Q(name__icontains=name)
        if country:
            filter_conditions &= Q(country__icontains=country)
        if marketing_channel:
            filter_conditions &= Q(marketing_channel__icontains=marketing_channel)
        if is_active is not None:
            filter_conditions &= Q(is_active=is_active.lower() == 'true')  # Convert 'true' string to boolean

        # Apply filters to the queryset
        campaigns = Campaign.objects.filter(filter_conditions)

        # Serialize the queryset and return response
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)
    except:
        message = {'detail': 'Error occurred'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
