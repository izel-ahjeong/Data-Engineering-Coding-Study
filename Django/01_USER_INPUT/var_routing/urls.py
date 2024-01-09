from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('greeting/<str:name>/', views.greeting),
    # <>가 받으면 변수가 되어 텍스트를 받을 수 있다.

    path('cube/<int:num>/', views.cube),

]
