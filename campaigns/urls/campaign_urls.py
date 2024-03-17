# campaign_urls.py

from django.urls import path
from campaigns.views import campaign_views as views

urlpatterns = [
    path('create', views.createOrUpdateCampaign, name='campaign-create'),
    path('', views.campaignDetails, name='details-campaigns'), 
]