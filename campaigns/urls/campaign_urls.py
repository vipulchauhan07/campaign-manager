# campaign_urls.py

from django.urls import path
from campaigns.views import campaign_views as views

urlpatterns = [
    path('campaigns/', views.getCampaign, name='get_campaigns'),  # GET endpoint to retrieve campaigns with filters
    path('campaigns/<int:campaign_id>/', views.getCampaign, name='get_campaign'),  # GET endpoint to retrieve a specific campaign
    path('campaigns/create/', views.createCampaign, name='create_campaign'),  # POST endpoint to create a new campaign
]
