from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from django.contrib.auth import logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User, Profile
from .serializers import UserRegistrationSerializer, UserSerializer, ProfileSerializer
from assessment.models import UserAssessmentData
from assessment.serializers import AssessmentSerializer



class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            print(user)
            token = RefreshToken.for_user(user)
            return Response({
                'status': True,
                'data': serializer.data,
                'message': 'Registration Successful, Please check email for activation link',
                'access': str(token.access_token),
            }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")   
        password = request.data.get('password')   

        user = User.objects.get(email=email)
        
        if not user:
            return Response({'status': False, 'msg': 'Invalid email'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'status': False, 'msg': 'Invalid password'})
        
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        response_data = {
            "message": "Log in successful",
            'access_token': str(access_token),
            "email": user.email,
            'first_name': user.first_name,
            "id": user.id,
        }

        return Response(response_data, status=status.HTTP_200_OK)
        


class LogoutView(GenericAPIView):
    """View that accepts a refresh token and blacklists it as a form of logout mechanism"""
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


class GetAllUsers(GenericAPIView):
    def get(self, request):
        try:
            qs = User.objects.all()
        except User.DoesNotExist:
            raise ValueError({
                'msg': 'Object does not exist' 
            })

        serializer = UserSerializer(qs, many=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
    
    
class UpdateProfileView(GenericAPIView):
    serializer_class = ProfileSerializer
    def patch(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'success': False, 'err': 'Profile does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = self.serializer_class(profile, partial=True, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': "profile updated successfully!",
                'data': serializer.data, 
                'status': status.HTTP_200_OK
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


