from django.contrib.auth import views as user_views
from django.urls import reverse_lazy
from django.views import generic as views

from Miniature_market.accounts.forms import CreateProfileForm


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home page')
    form_class = CreateProfileForm


class LoginUserView(user_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class LogoutUserView(user_views.LogoutView):
    template_name = 'accounts/logout.html'
    next_page = reverse_lazy('home page')
