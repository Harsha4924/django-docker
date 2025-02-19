from django.urls import path
from . import views

urlpatterns = [
    path('mydev/', views.my_func, name='my_func')
]
