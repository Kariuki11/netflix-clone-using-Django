from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-list/', views.add_to_list, name='add-to-list'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]
