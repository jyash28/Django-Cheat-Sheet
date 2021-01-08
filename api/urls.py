from django.urls import path
from . import views

urlpatterns=[
    path('posts/',views.users,name='users'),
    path('post/<int:pk>' ,views.users,name='user'),
]