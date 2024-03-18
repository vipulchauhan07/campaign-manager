# target_audience_urls.py

from django.urls import path
from campaigns.views import target_audience_views as views

urlpatterns = [
    path('create', views.createTargetAudience, name='audience-create'),
    path('get', views.getTargetAudiences, name='details-audience'), 
    path('update', views.updateTargetAudience, name='update-audience'),
]