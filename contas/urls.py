from django.urls import path
from django.contrib.auth import views as auth_views
from contas.views import UserLoginView, UserCreateView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('novo-usuario/', UserCreateView.as_view(), name='user_new'),

    path('passord-reset/', auth_views.PasswordResetView.as_view(
        template_name='reset/password_reset_form.html'), name='password_reset'
    ),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset/password_reset_confirm.html'), name='password_reset_confirm'
    ),
    path('passord-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset/password_reset_done.html'), name='password_reset_done'
    ),
    path('passord-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset/password_reset_complete.html'), name='password_reset_complete'
    ),
]
