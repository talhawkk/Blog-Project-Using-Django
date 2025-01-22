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
    path('addpost/', views.addpost, name='addpost'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('blog/<int:id>', views.readblog, name='readblog'),
    

]