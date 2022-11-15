from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('register2',views.register2,name='register2'),
]