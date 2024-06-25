from django.urls import  path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.tinder_base, name='home'),
    path('explore', views.search_users, name='explore'),
    path('explore/<int:people_id>/', views.detail_people, name='detail_people'),
    path('friend_request/<int:people_id>', views.friend_request, name='friend_request'),
    path('my_gifts', views.my_gifts, name='my_gifts'),
    path('friends', views.my_friends, name='friends'),
    
    ]