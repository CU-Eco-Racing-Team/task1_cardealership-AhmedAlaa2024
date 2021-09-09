from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:id>', views.index, name='index'),   
]