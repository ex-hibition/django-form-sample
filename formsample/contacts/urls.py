from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.get_contact, name='input'),
    path('thanks/', views.thanks, name='thanks'),
]
