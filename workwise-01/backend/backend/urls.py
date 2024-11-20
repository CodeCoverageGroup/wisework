from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.shortcuts import render

def home_view(request):
    """Show a simple home page"""
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/departments/', include('departments.urls')),
    path('api/machines/', include('machines.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/jobs/', include('jobs.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('server-home/', home_view),  # Already defined for backend server view
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]