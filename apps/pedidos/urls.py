from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from .views import CategoryViewSet, SuppliesViewSet, DocumentTypeViewSet, InvoiceViewSet, OrdersViewSet, OrderDetailsViewSet
from rest_framework import routers

'''
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'documenttype', DocumentTypeViewSet)
router.register(r'invoice', InvoiceViewSet)
router.register(r'order', OrdersViewSet)
router.register(r'orderdetails', OrderDetailsViewSet)
router.register(r'supplies', SuppliesViewSet)
#router.register(r'posts/<int:pk>', PostViewSet, basename='POST' )
#router.register(r'tags', TagViewSet)
'''

urlpatterns = [
    #router = routers.DefaultRouter()
    url(r'^category/$', CategoryViewSet),
    url(r'^documenttype/$', DocumentTypeViewSet),
    url(r'^invoice/$', InvoiceViewSet),
    url(r'^order/$', OrdersViewSet),
    url(r'^orderdetails/$', OrderDetailsViewSet),
    url(r'^supplies/$', SuppliesViewSet),    
    #path('pedidos/', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)