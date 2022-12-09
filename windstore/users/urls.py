from . import views
from django.contrib.auth.views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        views.SignUp.as_view(
            extra_context={
                'operation': 'Sign up'
            },

        ),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html',
            extra_context={
                'subtitle': ' - Sign In',
                'operation': 'Sign in'
            },
        ),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='done_message.html',
            extra_context={
                'msg': 'Вы вышли из своей учетной записи. Ждём Вас снова!'
            },
        ),
        name='logout'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            extra_context={
                'operation': 'Change password'
            },
        ),
        name='password_change_form'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='done_message.html',
            extra_context={
                'msg': 'Пароль успешно изменён!'
            },
        ),
        name='password_change_done'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset_form.html',
            extra_context={
                'operation': 'Reset password'
            },
        ),
        name='password_reset_form'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='done_message.html',
            extra_context={
                'msg': 'Проверьте свою почту, вам должно прийти письмо со ссылкой для восстановления пароля.'
            },
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            extra_context={
                'operation': 'Enter new password'
            },
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='done_message.html',
            extra_context={
                'msg': 'Пароль сохранён. Используйте его для входа.'
            },
        ),
        name='password_reset_complete'
    )
]