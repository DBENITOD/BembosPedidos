from django.shortcuts import render
from rest_framework import generics, viewsets, filters, permissions
from .models import Category ,Document_type, Invoice, Orders, Order_details, Supplies
from .serializers import CategorySerializers, SuppliesSerializers ,DocumentTypeSerializers, InvoiceSerializers, OrderDetailsSerializers, OrdersSerializers

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('description', )

class SuppliesViewSet(viewsets.ModelViewSet):
    serializer_class = SuppliesSerializers
    queryset = Supplies.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )

class DocumentTypeViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentTypeSerializers
    queryset = Document_type.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('description', )

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializers
    queryset = Invoice.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('order', )

class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializers
    queryset = Orders.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('nickname', )

class OrderDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailsSerializers
    queryset = Order_details.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id_orders', )