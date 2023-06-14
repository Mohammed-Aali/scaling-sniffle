from django.urls import path

from . import views

# gave the app a name so that we can use it in the url function
app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add')
]