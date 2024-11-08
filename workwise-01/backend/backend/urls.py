from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    """Show a simple home page"""
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),  # Authentication-related URLs
    path('api/departments/', include('departments.urls')),  # Department-related URLs
    path('api/machines/', include('machines.urls')),  # Machines-related URLs
    path('api/notifications/', include('notifications.urls')),  # Notifications-related URLs
    path('api/jobs/', include('jobs.urls')),  # Jobs-related URLs
    path('api/accounts/', include('accounts.urls')),
    path('', home_view),  # Homepage
]
