from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

##  app_name = 'account'  ## use namespace for other apps 

urlpatterns = [
    ## To use HTML version of email template  ## 
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(html_email_template_name='registration/password_reset_email_html.html'), 
         name='password_reset'), 
    path('', include('django.contrib.auth.urls')),
    # path('login/', auth_views.LoginView.as_view(), name='login'), 
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'), 
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), 
    # path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), 

    path('', views.dashboard, name='dashboard'), 
    path('register/', views.register, name='register'), 
    path('user_edit/', views.user_edit, name='user_edit'), 
    
]