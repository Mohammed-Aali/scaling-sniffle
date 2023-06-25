from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('create', views.create, name='create'),
    path('random', views.random, name='random'),
    path('<str:title>', views.pages, name='pages'),
    path('edit:<str:page>', views.edit, name='edit'),
]
