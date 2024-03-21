from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  UserRegistrationSerializer

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