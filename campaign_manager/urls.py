from django.urls import path, include
from django.contrib import admin
# from campaigns import admin  # Uncomment this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/campaign', include('campaigns.urls.campaign_urls')),
    path('api/target-audience', include('campaigns.target_audience_urls')),
]
