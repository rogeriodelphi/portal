from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_url = '/index/'
    success_message = "Login efetuado com sucesso!"



# Create your views here.
