from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.aboutus , name='aboutus'),
    path('contact/', views.contactus , name='contactus'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('signup/', views.user_signup , name='signup'),
    path('login/', views.user_login , name='login'),
    path('logout/', views.user_logout , name='logout'),
]