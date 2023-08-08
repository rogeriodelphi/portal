from django.urls import path
from django.contrib.auth import views as auth_views
from contas.views import UserLoginView, UserCreateView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('novo-usuario/', UserCreateView.as_view(), name='user_new'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='reset/password_change_done.html'), name='password_change_done'
    ),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='reset/password_reset_form.html'), name='password_reset'
    ),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset/password_reset_confirm.html'), name='password_reset_confirm'
    ),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset/password_reset_done.html'), name='password_reset_done'
    ),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset/password_reset_complete.html'), name='password_reset_complete'
    ),
    path('password_change/', auth_views.PasswordResetView.as_view(
        template_name='reset/password_form.html'), name='password_change'
    ),
]
