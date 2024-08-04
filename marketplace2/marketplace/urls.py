# marketplace/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('marketplace_one.urls')),  # Подставьте имя вашего приложения вместо your_app_name
]

