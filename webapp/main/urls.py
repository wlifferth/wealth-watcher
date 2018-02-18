from django.urls import path

from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('users/', views.users, name='users'),
    path('user/<str:user_id>/', views.user, name='user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('alerts/', views.alerts, name='alerts'),
    path('alert/<purchase_id>/', views.alert, name='alert'),
    path('resolve/<purchase_id>/<resolution>/', views.resolve, name='resolve'),
    path('run_learning', views.run_learning, name='run-learning'),
    path('run_rules/', views.run_rules, name='run-rules'),
    path('run_sync/', views.run_sync, name='run-sync'),
    path('login/', views.log_in, name='login'),
]
