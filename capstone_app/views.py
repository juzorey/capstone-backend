from .serializers import UsersSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.

class UsersList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer