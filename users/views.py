from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from .serializers import UserRegistrationSerializer

# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'detail': 'User registration successful'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Authenticate the user
            authenticated_user = authenticate(
                request,
                username=request.data['username'],
                password=request.data['password']
            )

            # Check if authentication was successful before logging in
            if authenticated_user is not None:
                login(request, authenticated_user)
                return Response({'detail': 'User registration and login successful'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'User registration successful, but login failed'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request):
#         user = request.user
#         login(request, user)
#         return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             # Check if the user is active before logging in
#             if user.is_active:
#                 login(request, user)
#                 print(user)
#                 return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'detail': 'Inactive user'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            # Generate or get the existing token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)


"""
{
  "username": "john_doe",
  "email": "john.doe@example.com",
  "password": "securepassword123"
}

"""