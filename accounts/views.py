from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView
# from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .serializers import UserRegistrationSerializer, UserSerializer
from django.urls import reverse
from assessment.models import Assessment
from assessment.serializers import AssessmentSerializer


class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request):
        data = request.data 
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'data': serializer.data,
                'message': 'Account successfully created'
            }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    # authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    # csrf_exempt = True

    def post(self, request, *args, **kwargs):
        # Get username and password from the request
        email = request.data.get("email")
        password = request.data.get("password")

        # Authenticate the user
        user = authenticate(email=email, password=password)
        

        if user is not None:
            # If authentication is successful, create or retrieve a token
            refresh = RefreshToken.for_user(user)
            try:
                qs = Assessment.objects.get(user=user)
                serializer = AssessmentSerializer(qs)
                print(serializer)
            except Assessment.DoesNotExist:
                serializer = AssessmentSerializer()

            login(request, user)  # Optional: Log the user in
            response_data = {
                "message": "Log in successful",
                "statusCode": status.HTTP_200_OK,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                "email": user.email,
                'first_name': user.first_name,
                "id": user.id,
                # "isAdmin": user.is_staff  # Assuming 'is_staff' signifies admin status
                'assessment_data': serializer.data,
                }
 
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED,
            )
        

# This logout view only blacklists the refresh token, and has no
# effect on the access token. In the future, the access token's
# lifespan would be reduced to restrict acess to both tokens
# within a reasonable timeframe.
class LogoutView(APIView):
    """View that accepts a refresh token and blacklists it as a form of logout mechanism"""

    # So authentication credentials are not required to blacklist a token
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token') or request.data.get('refresh')
        if not refresh_token:
            return Response({'error':'Request token not provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            return Response({'message':'User Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetAllUsers(APIView):
    def get(self, request):
        try:
            qs = User.objects.all()
        except User.DoesNotExist:
            raise ValueError({
                'message': "Object does not exist!!"
            })

        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)