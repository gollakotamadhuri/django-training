from django.urls import path

from . import views

urlpatterns = [
    path('help/', views.help, name="help"),
    path('', views.index, name="index"),
    path('users/', views.user, name="users"),
    path("signup/", views.signup, name="signup")
]
