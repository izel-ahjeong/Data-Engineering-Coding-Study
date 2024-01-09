from django.urls import path
from . import views

urlpatterns = [
    path('bmi_in/', views.bmi_in),
    path('bmi_out/', views.bmi_out),
]