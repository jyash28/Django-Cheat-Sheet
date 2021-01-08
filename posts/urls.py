from django.urls import path
from posts.views import index,cbview

urlpatterns =[
    path('',index,name='index'),
    path('cbview/',cbview.as_view(),name="cbview")
]