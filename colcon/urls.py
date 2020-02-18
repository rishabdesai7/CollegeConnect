from django.urls import path

from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('resetpassword/<str:id>/<str:pwd>',views.reset_password,name='resetpwd'),
    path('forgotpassword/<str:id>',views.forgot_password,name = 'forgotpwd'),
    path('activate/<str:id>',views.activate,name = 'activate'),
    path('logout',views.logout,name='logout'),
    path('ppu',views.profile_picture_upload,name = 'ppu'),
    path('channelList',views.channel_list,name = 'cl'),
    path('addPost',views.add_post,name = 'ap'),
    path('getPost/<str:channel_name>',views.get_posts,name ='po'),
    path('addComment',views.add_comment,name = 'ac'),
    path('getComment/<int:postid>',views.get_comments,name = 'gc'),
    path('addChannelRequest',views.add_channel_request,name = 'acr'),
    path('addComplaint',views.add_complaint,name = 'acp'),
]