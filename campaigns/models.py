from django.db import models
from django.utils import timezone

# Create your models here.

class GenderType(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"

class MarketingChannel(models.TextChoices):
    EMAIL = "EMAIL", "E-mail"
    PHONE = "PHONE", "Phone Number"

class Campaign(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = models.CharField(max_length=50)
    marketing_channel = models.CharField(max_length=50, choices=MarketingChannel.choices)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default= None)
    class Meta:
        # Specify the desired table name
        db_table = 'campaign'

class TargetAudience(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    gender_type = models.CharField(max_length=10, choices=GenderType.choices)
    class Meta:
        # Specify the desired table name
        db_table = 'target_audience'

class Owner(models.Model):
    owner_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    class Meta:
        # Specify the desired table name
        db_table = 'owner'

class CampaignOwner(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    class Meta:
        # Specify the desired table name
        db_table = 'campaign_owner'
