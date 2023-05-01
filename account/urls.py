from django.urls import path
from account import views as account_view

urlpatterns = [
    path('', account_view.index, name='index'),
    path('login/', account_view.user_login, name='login'),
    path('logout/', account_view.user_logout, name='logout'),
    path('register/', account_view.user_register, name='register'),
    path('dashboard/', account_view.dashboard, name='dashboard'),

]
