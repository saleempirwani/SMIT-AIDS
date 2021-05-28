from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="shopHome"),
    path('product/', views.product, name="shopProduct"),
    path('about/', views.about, name="shopAbout"),
]