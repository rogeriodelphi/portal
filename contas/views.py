from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = template_name = 'registration/login.html'


# Create your views here.
