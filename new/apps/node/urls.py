from django.urls import path
from . import views

app_name="node"

urlpatterns = [
    path('', views.home, name='home'), 
    path('change/', views.change, name='change')
]
