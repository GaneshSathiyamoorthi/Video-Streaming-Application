from django.urls import path
from videoapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', views.video_list, name='video_list'),
    path('videos/<int:id>/', views.video_detail, name='video_detail'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('videos/delete/<int:id>/', views.delete_video, name='delete_video'),
    path('videos/search/', views.search_videos, name='search_videos'),
    path('videos/upload/', views.upload_video, name='upload_video'),


]

