from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import UserCreateView
from .forms import LoginForm
from . import views

urlpatterns = [
    # accounts templates
    path(
        'login/',
        auth_views.LoginView.as_view(template_name="accounts/login.html",
                                     form_class=LoginForm),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name='logout'
    ),
    path(
        'new_account/',
        UserCreateView.as_view(),
        name='create_account'
    ),

    # change_pass templates
    path(
        'accounts/change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change_pass/password_change_form.html'),
        name='password_change'
    ),
    path(
        'accounts/password_changed/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='change_pass/password_change_done.html'),
        name='password_change_done'
    ),

    # reset_pass templates
    path(
        'accounts/forget_password/',
        auth_views.PasswordResetView.as_view(
            template_name='reset_pass/password_reset_form.html'),
        name='password_reset'
    ),
    path(
        'accounts/forget_password/email_sent',
        auth_views.PasswordResetDoneView.as_view(
            template_name='reset_pass/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'accounts/confirm_password/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='reset_pass/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'accounts/new_password/',
        auth_views.PasswordResetView.as_view(
            template_name='reset_pass/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
