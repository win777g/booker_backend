from django.shortcuts import render

# Create your views here.
from .models import *
from rest_framework import viewsets,permissions,generics
from bill.serializers import BillSerializer


class BillViewSet(viewsets.ModelViewSet):

    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
