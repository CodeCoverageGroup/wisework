from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    """Simple view for the root path"""
    return HttpResponse("Welcome to the Workwise backend!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/departments/', include('departments.urls')),
    path('api/machines/', include('machines.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/jobs/', include('jobs.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('server-home/', home_view),  # Already defined for backend server view
    path('', home_view),  # Add this to handle requests to the root `/`
]