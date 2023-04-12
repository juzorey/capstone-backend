from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('userslist/', views.UsersList.as_view(), name='users_list'),
    path('usersdetail/<int:pk>/',views.UsersDetail.as_view(), name='users_detail'),
]