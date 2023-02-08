#login_app/urls.py
from . import views
from django.urls import path
from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),

    path('', views.index, name='index'),  # ログイン後に行いたい処理
    path('login/', views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),  # Social Django用
]