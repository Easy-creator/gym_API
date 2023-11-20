from django.urls import path
from .views import LoginView, LogoutView, UserRegistrationView
from django.views.decorators.csrf import csrf_exempt

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
