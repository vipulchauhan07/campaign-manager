from django.urls import path, include
from django.contrib import admin
# from campaigns import admin  # Uncomment this line

urlpatterns = [
     path('admin/', admin.site.urls),
    path('api/', include('campaigns.urls')),
     path('', include('campaigns.urls')),
]
