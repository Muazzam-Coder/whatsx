# whatsX_advanced_prototype/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # This line provides the 'login', 'logout', etc. URL names
    path('accounts/', include('django.contrib.auth.urls')),
]