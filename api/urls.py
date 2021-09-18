from django.contrib import admin
from django.db.models.query import prefetch_related_objects
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'expenses', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path(r'', include(router.urls)),
]
