from django.urls import path
from . import views

urlpatterns = [
    path('', views.allforums, name='allforums'),
    path('<int:forums_id>/', views.detail, name='detailforum'),
]