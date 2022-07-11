from django.urls import path
from . import views

urlpatterns = [
    path('customer/',views.customer_list),
    path('customer/<int:id>/',views.customer_detail)
]