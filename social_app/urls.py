from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index.html'),
    path('settings', views.settings, name='setting.html'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout')
]
