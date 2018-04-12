from rest_framework import generics
from rest_framework.permissions import AllowAny
from custumer.models import Profile, User
from custumer.api.serializers import (
    CreateProfileSerializer,
    CreateUserSerializer,
    UpdateProfileSerializer
)


class CreateUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UpdateProfile(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [AllowAny]


class CreateProfile(generics.CreateAPIView):
    serializer_class = CreateProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [AllowAny]
