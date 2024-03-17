from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/campaigns/', include('campaigns.urls.campaign_urls')),
    # path('api/target-audience', include('campaigns.target_audience_urls')),
]
