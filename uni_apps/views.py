from django.shortcuts import render
from rest_framework import generics
from .serializers import ApplicantSerializer, ApplicationSerializer
from .models import Applicant, Application
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializers import UserSerializer
User = get_user_model()

# Create your views here.
class ApplicantList(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class ApplicantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ApplicantSerializer

class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ApplicantSerializer

class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})