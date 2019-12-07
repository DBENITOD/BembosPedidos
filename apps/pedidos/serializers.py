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

class OrderDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order_details
        fields=['id','quantity','id_orders','sub_total','id_supplies']
        #fields = '__all__'

class OrdersSerializers(serializers.ModelSerializer):
    comprobanted = OrderDetailsSerializers(many=True)    
    class Meta:
        model = Orders
        fields =['id','price','nickname','id_invoice','comprobanted']
        #fields = '__all__'


class SuppliesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Supplies
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class InvoiceSerializers(serializers.ModelSerializer):
    comprobante = OrdersSerializers(many=True)
    class Meta:
        model = Invoice
        fields = ['id','order','client_name','total','id_user','id_document_type','document_number','document_number','status','comprobante']
        #fields = '__all__'

    '''def create(self, validated_data):
        invoice = Invoice( id=validated_data.get("id") )
        invoice.save()        
        ord = validated_data.get('id_invoice')
        for ors in ord:
          Orders.objects.create(invoice=invoice, **ors)
        return validated_data'''