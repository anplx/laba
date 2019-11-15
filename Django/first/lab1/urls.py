from django.urls import path, re_path
from . import views
urlpatterns = [
    re_path('upload/$', views.createFolder),
    re_path('create/$', views.createFolder),
    re_path('create$', views.createFolder),
    re_path('delete/$', views.deleteFolder),
    re_path('delete$', views.deleteFolder),
    re_path('download/$', views.download),
    re_path('download$', views.download),
    re_path(r'^', views.directory),
    #re_path('create/$', views.createFolder),
]
