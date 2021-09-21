from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('login_page/', views.loginPage, name='login_page'),
    path('password_reset/', views.passwordReset, name='password_reset'),
    path('logout/', views.logoutUser, name='logout'),
    path('operators/', views.operators, name='operators'),
    url(r'^delete_operator/(?P<operator_id>[0-9]+)/$', views.delete_operator, name='delete_operator'),
    path('invalid_subscription/', views.not_subscribed, name='not_subscribed'),
]