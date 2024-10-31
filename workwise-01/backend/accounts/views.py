from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer


# User Serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


# User Registration View
class RegisterUserView(APIView):
    """
    API View to handle user registration.
    Allows anyone to register a new user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handle POST request to register a new user.
        Returns a success message or an error if the username already exists.
        """
        pass


# Protected View Example
class ProtectedView(APIView):
    """
    API View for a protected endpoint.
    Only authenticated users can access this view.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Handle GET request for authenticated users.
        Returns a success message if the user is authenticated.
        """
        pass


# User Detail (Read/Update/Delete) View
class UserDetailView(APIView):
    """
    Retrieve, update or delete a user instance.
    Only accessible by authenticated users.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        Retrieve a user by their primary key (pk).
        """
        pass

    def put(self, request, pk):
        """
        Update a user's details.
        """
        pass

    def delete(self, request, pk):
        """
        Delete a user by their primary key (pk).
        """
        pass


# List Users View (Admin only)
class UserListView(generics.ListAPIView):
    """
    List all users. Only accessible to admin users.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
