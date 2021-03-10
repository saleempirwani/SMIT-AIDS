from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="shopHome"),
    path('about/', views.about, name="shopAbout"),
]