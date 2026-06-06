from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('rgb/', views.rgb_auth, name='rgb'),
    path('image-auth/', views.image_auth, name='image_auth'),
    path('dashboard/', views.dashboard, name='dashboard'),
]