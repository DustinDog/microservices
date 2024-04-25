from accounts.models import User
from accounts.serializers import CreateUserSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        access_token = user.create_jwt_token()

        return Response(
            {
                "access": str(access_token),
            }
        )


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
