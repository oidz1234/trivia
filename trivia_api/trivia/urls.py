from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/test/', views.test, name='test'),
    path('api/capital/', views.capital, name='capital'),
]
