from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("blog/<str:pk>", views.blog, name='blog'),

    path('publish-blog/', views.publishBlog, name='publish-blog'),
    path('update-blog/<str:pk>', views.updateBlog, name='update-blog'),
    path('delete-blog/<str:pk>', views.deleteBlog, name='delete-blog'),


    path('user-profile/<str:pk>', views.userProfile, name='user-profile'),
    path('edit-profile/<str:pk>', views.editProfile, name='edit-profile'),

    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout')
]