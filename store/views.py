from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Customer
from .serializers import CustomerSerializer
# Create your views here.

@api_view()
def customer_list(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer,many=True)
    return Response(serializer.data)

@api_view()
def customer_detail(request,id):
    try:
        customer = Customer.objects.get(pk=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data) 
    except Customer.DoesNotExist:
        return Response(status=404)
