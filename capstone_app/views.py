from .serializers import UsersSerializer
from .serializers import FoodSerializer
from .models import User, Food
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import jwt, datetime

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data={'message:logged out successfully'}
        return response


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'id'

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        user = User.objects.get(id=user_id)
        return user

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request': request})
        return Response(serializer.data)
    



class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer




# class HomeView(APIView):
#     permission_classes = (IsAuthenticated, )

#     def get(self, request):
#         content = {
#             'message': 'Welcome to BabyBliss!'},
#         return Response(content)


# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated, )

#     def post(self, request):

#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


# class UserView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             access = refresh.access_token
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(access),
#             })
#         else:
#             return Response(serializer.errors, status=400)


# class CreateUserView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         if not username or not password:
#             return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
#         user = User.objects.create_user(username=username, password=password)
#         return Response({'message': f'User {user.username} created successfully'}, status=status.HTTP_201_CREATED)

# class UsersList(generics.ListCreateAPIView):
#     permission_classes = [AllowAny]
#     queryset = User.objects.all()
#     serializer_class = UsersSerializer

# class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UsersSerializer