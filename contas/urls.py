from django.urls import path
from django.contrib.auth import views as auth_views
from contas.views import UserLoginView, UserCreateView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('novo-usuario/', UserCreateView.as_view(), name='user_new'),
]
