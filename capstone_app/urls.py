from django.urls import path
from . import views
from .views import RegisterView
from .views import FoodList
from .views import FoodDetail
from .views import LoginView
from .views import UserView
from .views import LogoutView
from .views import UserDetail
from .views import UserList

from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('home/', views.HomeView.as_view(), name='home'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('api/user/', views.UserView.as_view(), name='user'),
    # path('createuser/', views.CreateUserView.as_view(), name='createuser'),
    # path('userslist/', views.UsersList.as_view(), name='users_list'),
    # path('usersdetail/<int:pk>/',views.UsersDetail.as_view(), name='users_detail'),
    path('/register/', views.RegisterView.as_view()),
    path('/login/', views.LoginView.as_view()),
    path('/user/', views.UserView.as_view(), name="user_detail"),
    path('/userslist/', views.UserList.as_view()),
    path('/users/<int:user_id>/', views.UserDetail.as_view()),
    path('/logout/', views.LogoutView.as_view()),
    path('/foods/', views.FoodList.as_view()),
    path('/fooddetails/<int:pk>',views.FoodDetail.as_view()),
    ]