from datetime import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer
from django.utils import timezone
import logging


@api_view(['POST', 'PUT'])
def createOrUpdateCampaign(request):
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
    except Campaign.DoesNotExist as e:
        # Handle the case where the campaign with the given ID does not exist
        logging.error(f"Campaign does not exist: {e}")
        return Response({"detail": "Campaign does not exist."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Log the specific exception and return a generic error message
        logging.error(f"An error occurred: {e}")
        return Response({"detail": "An error occurred."}, status=status.HTTP_400_BAD_REQUEST)


""" @api_view(['GET'])
def campaignDetails(request):
    try:
        # Retrieve query parameters from the request
        id = request.query_params.get('id', None)
        name = request.query_params.get('name', None)
        country = request.query_params.get('country', None)
        marketing_channel = request.query_params.get('marketing_channel', None)
        is_active = request.query_params.get('active', None)

        # Build filter conditions
        filter_conditions = Q()
        if id:
            filter_conditions &= Q(name__icontains=id)
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
        return Response(message, status=status.HTTP_400_BAD_REQUEST) """

@api_view()
def campaignDetails(request):
    try:
        # Retrieve query parameters from the request
        id = request.query_params.get('id')
        name = request.query_params.get('name')
        country = request.query_params.get('country')
        marketing_channel = request.query_params.get('marketing_channel')
        is_active = request.query_params.get('active')

        # Build filter conditions
        filter_conditions = Q()
        if id:
            filter_conditions &= Q(id=id)
        if name:
            filter_conditions &= Q(name__icontains=name)
        if country:
            filter_conditions &= Q(country__icontains=country)
        if marketing_channel:
            filter_conditions &= Q(marketing_channel__icontains=marketing_channel)
        if is_active is not None:
            is_active_bool = is_active.lower() == 'true'
            filter_conditions &= Q(is_active=is_active_bool)

        # Apply filters to the queryset
        campaigns = Campaign.objects.filter(filter_conditions)

        # Serialize the queryset and return response
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return Response({"detail": "An error occurred."}, status=status.HTTP_400_BAD_REQUEST)