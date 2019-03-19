from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.pagina, {'slug': 'sobre'}, name='sobre'),
    path('pagina/<str:slug>/', views.pagina, name='pagina'),
]
