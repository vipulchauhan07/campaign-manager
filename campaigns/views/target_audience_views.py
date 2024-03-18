import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from campaigns.models import TargetAudience
from campaigns.serializers import TargetAudienceSerializer
from django.db.models import Q

logger = logging.getLogger(__name__)

# POST API to create a new target audience
@api_view(['POST'])
def createTargetAudience(request):
    try:
        serializer = TargetAudienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.exception("An error occurred while creating a new target audience.")
        return Response({"detail": "An error occurred while creating a new target audience."}, status=status.HTTP_400_BAD_REQUEST)

# GET API to retrieve a list of target audiences with optional filters
@api_view(['GET'])
def getTargetAudiences(request):
    try:
        name = request.query_params.get('name')
        email = request.query_params.get('email')
        age = request.query_params.get('age')
        gender_type = request.query_params.get('gender_type')

        filter_conditions = Q()
        if name:
            filter_conditions &= Q(name__icontains=name)
        if email:
            filter_conditions &= Q(email__icontains=email)
        if age:
            filter_conditions &= Q(age=age)
        if gender_type:
            filter_conditions &= Q(gender_type=gender_type)

        target_audiences = TargetAudience.objects.filter(filter_conditions)
        serializer = TargetAudienceSerializer(target_audiences, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.exception("An error occurred while retrieving target audiences.")
        return Response({"detail": "An error occurred while retrieving target audiences."}, status=status.HTTP_400_BAD_REQUEST)

# PUT API to update an existing target audience
@api_view(['PUT'])
def updateTargetAudience(request):
    try:
        data = request.data
        audience_id = data.get('id')
        target_audience = TargetAudience.objects.get(pk=audience_id)
        serializer = TargetAudienceSerializer(target_audience, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except TargetAudience.DoesNotExist:
        return Response({"detail": "Target audience not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception("An error occurred while updating the target audience.")
        return Response({"detail": "An error occurred while updating the target audience."}, status=status.HTTP_400_BAD_REQUEST)