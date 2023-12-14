from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('remove/city/<int:id>', views.remove_city),
]