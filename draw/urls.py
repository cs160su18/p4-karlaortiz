# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#     url(r'^$', views.customInteraction, name='customInteraction'),
    path('smallInteraction1/', views.smallInteraction1, name='smallInteraction1'),
    path('smallInteraction2/', views.smallInteraction2, name='smallInteraction2'),
    path('largeDisplay/', views.largeDisplay, name='largeDisplay'),
    path('teacherDisplay/', views.teacherDisplay, name='teacherDisplay'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

