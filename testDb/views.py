from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        response_data = {
            "isSuccess": True,
            "message": "Users retrieved successfully",
            "data": serializer.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        response_data = {
            "isSuccess": True,
            "message": "User retrieved successfully",
            "data": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "isSuccess": True,
                "message": "User created successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                "isSuccess": False,
                "message": "User creation failed",
                "data": serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        data = request.data
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "isSuccess": True,
                "message": "User updated successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "isSuccess": False,
                "message": "User update failed",
                "data": serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        user.delete()
        response_data = {
            "isSuccess": True,
            "message": "User deleted successfully",
            "data": None
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def updateProfile(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        data = request.data
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "isSuccess": True,
                "message": "Profile updated successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "isSuccess": False,
                "message": "Profile update failed",
                "data": serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
