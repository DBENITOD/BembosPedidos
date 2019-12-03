# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.
'''class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    status = models.CharField(max_length=10, blank=False, null=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['name']

    def __str__(self):
        return self.nombre'''

'''class User(models.Model):
    id = models.AutoField(primary_key=True)
    names= models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    rol_id = models.ManyToManyField(Rol, through='RolUser', through_fields=('user_id', 'rol_id'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.names} {self.lastname}'

class RolUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Rol User'
        verbose_name_plural = 'Roles Users'

    def __str__(self):
        return f'{self.usuario_id} / {self.rol_id}

class RolUsuario_inline(admin.TabularInline):
    model = RolUsuario
    extra = 1

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (RolUsuario_inline,)'''

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['description']

    def __str__(self):
        return self.description

#####FALTA DEFINIR LA RUTA PARA  SUBIR LA IMAGEN Y EL TAMAÑO QUE TENDRÁ LA IMAGEN######

class Supplies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='Pictures/Supplies',blank=True, null=False)
    quantity = models.IntegerField()
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Supplies'
        verbose_name_plural = 'Supplies'
        ordering = ['name']

    def __str__(self):
        return self.name



class Document_type(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Document_type'
        verbose_name_plural = 'Document_types'
        ordering = ['id']

    def __str__(self):
        return self.description


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.BigIntegerField(blank=False, null=False)
    client_name = models.CharField(max_length=50)
    #orde = models.CharField(max_length=18)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_document_type = models.ForeignKey(Document_type, on_delete=models.CASCADE)
    document_number = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        ordering = ['order']

    def __str__(self):
        return self.order

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    #cod_order = models.CharField(max_length=18)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    nickname = models.CharField(max_length=30)
    id_invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['id']

    def __str__(self):
        return self.nickname


class Order_details(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(blank=False, null=False)
    id_orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=12, decimal_places=2)
    id_supplies = models.ForeignKey(Supplies, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Order Details'
        verbose_name_plural = 'Orders Details'
        ordering = ['id_orders']

    def __str__(self):
        return self.id_orders