from django.urls import path

from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('users/', views.users, name='users'),
    path('user/<str:user_id>/', views.user, name='user'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
