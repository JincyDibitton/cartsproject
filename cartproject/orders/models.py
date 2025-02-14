from django.db import models
from customers.models import Customer
from products.models import Products

# Create your models here.

class Order(models.Model):
    LIVE=1
    DELETE=0
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERERD=3
    ORDER_REJECTED=4
    STATUS_CHOICES=((ORDER_PROCESSED,'ORDER_PROCESSED'),
                    (ORDER_DELIVERERD,'ORDER_DELIVERERD'),
                    (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class OrderedItem(models.Model):
    products=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,related_name='added_carts')    
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

