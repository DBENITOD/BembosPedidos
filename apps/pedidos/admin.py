from django.contrib import admin
from .models import Document_type, Invoice, Orders, Order_details, Supplies

# Register your models here.
admin.site.register(Document_type)
admin.site.register(Invoice)
admin.site.register(Orders)
admin.site.register(Order_details)
admin.site.register(Supplies)