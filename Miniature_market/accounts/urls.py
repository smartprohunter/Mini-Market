from django.urls import path

from Miniature_market.accounts.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns =(
    path('create/', RegisterUserView.as_view(), name='register page'),
    path('login/', LoginUserView.as_view(), name='login page'),
    path('logout/', LogoutUserView.as_view(), name='logout page')
)