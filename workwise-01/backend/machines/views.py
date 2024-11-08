# pylint: disable=no-member
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Machine, MaintenanceTicket
from .serializers import MachineSerializer, MaintenanceTicketSerializer

class MachineViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Machine instances.

    Provides CRUD operations for the Machine model, allowing authenticated
    users to create, retrieve, update, and delete machines.

    Attributes:
        queryset (QuerySet): The base queryset for retrieving Machine records.
        serializer_class (Serializer): The serializer used to validate and serialize Machine data.
        authentication_classes (list): Specifies JWT-based authentication.
        permission_classes (list): Restricts access to authenticated users only.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class MaintenanceTicketViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing MaintenanceTicket instances.

    Provides CRUD operations for the MaintenanceTicket model, allowing
    authenticated users to create, retrieve, update, and delete maintenance tickets.

    Attributes:
        queryset (QuerySet): The base queryset for retrieving MaintenanceTicket records.
        serializer_class (Serializer): The serializer used to validate and serialize MaintenanceTicket data.
        authentication_classes (list): Specifies JWT-based authentication.
        permission_classes (list): Restricts access to authenticated users only.
    """
    queryset = MaintenanceTicket.objects.all()
    serializer_class = MaintenanceTicketSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
