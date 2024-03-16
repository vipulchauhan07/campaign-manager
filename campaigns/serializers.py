from rest_framework import serializers
from .models import Campaign, TargetAudience, Owner, CampaignOwner

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class TargetAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetAudience
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class CampaignOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignOwner
        fields = '__all__'
