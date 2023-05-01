from django.urls import path
from account import views as account_view

urlpatterns = [
    path('', account_view.index, name='index'),

]
