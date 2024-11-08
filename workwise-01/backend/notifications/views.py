# pylint: disable=no-member
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Notification instances.

    Provides CRUD operations for notifications, allowing authenticated users 
    to create, retrieve, update, and delete notifications. Each user can only 
    access their own notifications, ordered by creation date in descending order.
    
    Attributes:
        queryset (QuerySet): The base queryset for retrieving Notification records, 
                             ordered by `created_at` in descending order.
        serializer_class (Serializer): The serializer used to validate and 
                                       serialize Notification data.
        permission_classes (list): Restricts access to authenticated users only.
    """

    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset of notifications for the authenticated user.

        Overrides the default `get_queryset` method to filter notifications 
        so that users can only access their own notifications.

        Returns:
            QuerySet: A queryset of Notification objects belonging to the current user.
        """
        return self.queryset.filter(user=self.request.user)
