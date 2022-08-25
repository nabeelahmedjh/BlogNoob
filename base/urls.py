from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("blog/<str:pk>", views.blog, name='blog'),

    path('publish-blog/', views.publishBlog, name='pubish-blog'),


    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout')
]