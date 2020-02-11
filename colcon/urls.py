from django.urls import path

from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('resetpassword/<str:id>/<str:pwd>',views.reset_password,name='resetpwd'),
    path('forgotpassword/<str:id>',views.forgot_password,name = 'forgotpwd'),
    path('activate/<str:id>',views.activate,name = 'activate'),
]