# campaign_urls.py

from django.urls import path
from campaigns.views import campaign_views as views

urlpatterns = [
    path('campaigns/', views.getCampaign, name='get_campaigns'),  # GET endpoint to retrieve campaigns with filters
    path('campaigns/<int:campaign_id>/', views.createOrUpdateCampaign, name='create_or_update_campaign'),  # POST and PUT endpoint to create or update a campaign
]