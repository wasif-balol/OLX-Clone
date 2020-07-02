from django.urls import path
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'
urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='assword_change'),
    # path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']

]
