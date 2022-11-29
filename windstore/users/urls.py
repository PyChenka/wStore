from . import views
from django.contrib.auth.views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        views.SignUp.as_view(),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html',
            extra_context={'subtitle': ' - Sign In'},),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='users/logged_out.html',
            extra_context={'subtitle': ''},
        ),
        name='logout'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            extra_context={'subtitle': ''},
        ),
        name='password_change_form'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
            extra_context={'subtitle': ''},
        ),
        name='password_change_done'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset_form.html',
            extra_context={'subtitle': ''},
        ),
        name='password_reset_form'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html',
            extra_context={'subtitle': ''},
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            extra_context={'subtitle': ''},
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html',
            extra_context={'subtitle': ''},
        ),
        name='password_reset_complete'
    )
]