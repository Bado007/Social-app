from django.contrib import admin
from django.urls import path
from social_app import views


urlpatterns = [
    path('', views.index, name='index.html'),
    path('settings', views.settings, name='setting.html'),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout')
]
