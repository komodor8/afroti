from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexSplashScreen.as_view(), name='index'),
    path('home/', views.IndexSplashScreen.as_view(), name='index'),
    path('plats-a-emporter/', views.IndexFood.as_view(), name='plats-a-emporter'),
    path('gateaux/', views.IndexCake.as_view(), name='gateaux'),
]
