from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import JsonResponse
from django.contrib.auth import login, logout,authenticate 

class UserRegistrationAPIView(APIView):
    def post(self, request):
        user_serializer = UserRegistrationSerializer(data=request.data)

        if user_serializer.is_valid():
            user = user_serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            if not user_serializer.is_valid():
                errors.update(user_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        


class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "User logged in successfully."})
        else:
            return JsonResponse({"message": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return JsonResponse({"message": "User logged out successfully."})