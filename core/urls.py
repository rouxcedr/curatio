from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('login_page/', views.loginPage, name='login_page'),

    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), name='password_reset_complete'),

    path('forgot_username', views.forgot_username, name="forgot_username"),

    path('logout/', views.logoutUser, name='logout'),
    path('invalid_subscription/', views.not_subscribed, name='not_subscribed'),
    # path('max_operator/', views.max_operator, name="max_operator"),
    path('register/<data>/', views.registerPage, name='register_page'),

    path('send_operateur_regsitration_email', views.sendOperatorRegistrationEmail, name="send_operator_registration_email"),

    path('profile/', views.ProfilePage, name='profile_page')
]