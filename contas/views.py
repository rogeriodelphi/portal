from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from contas.admin import UserCreationForm
from contas.models import MyUser


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_url = '/index/'
    success_message = "Login efetuado com sucesso!"

class UserCreateView(SuccessMessageMixin, CreateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = 'registration/user_new.html'
    success_url = reverse_lazy('index')
    success_message = 'Cadastro efetuado com sucesso.'
