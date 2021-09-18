from rest_framework import serializers
from .models import *

class ExpenseSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source= 'creator.username', required=False, read_only=True)

    class Meta:
        model = Expense
        fields = ('id', 'creator', 'amount', 'month',)      