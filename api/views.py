from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.generics import *
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Expense.objects.all()
