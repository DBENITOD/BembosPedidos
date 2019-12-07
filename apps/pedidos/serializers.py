from rest_framework import serializers
from .models import Document_type,Category, Invoice, Orders, Order_details, Supplies
from django.contrib.auth.models import User


class DocumentTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document_type
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order_details
        fields = '__all__'

class SuppliesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Supplies
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'