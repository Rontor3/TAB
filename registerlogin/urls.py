from django.urls import path
from registerlogin import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="Login"),
    path("logout", views.logout, name="Logout"),
    path("verify/<auth_token>", views.verify, name='verify'),
    path('token', views.token_send, name="token_send"),
    path('success', views.success, name='success'),
    path('error', views.error, name="error")

]
