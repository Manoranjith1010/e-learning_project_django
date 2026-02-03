"""
Serializers for finance
"""

from rest_framework import serializers
from .models import Payment, Invoice


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_method', 'status', 'created_at']
        read_only_fields = ['status']


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'amount', 'tax', 'total', 'issued_date', 'due_date']
