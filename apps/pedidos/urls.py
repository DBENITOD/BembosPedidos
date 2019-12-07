from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from .views import CategoryViewSet, SuppliesViewSet, DocumentTypeViewSet, InvoiceViewSet, OrdersViewSet, OrderDetailsViewSet
from .views import UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('documenttype', DocumentTypeViewSet)
router.register('invoice', InvoiceViewSet)
router.register('order', OrdersViewSet)
router.register('orderdetails', OrderDetailsViewSet)
router.register('supplies', SuppliesViewSet)
router.register('user', UserViewSet)
urlpatterns = [

    path('pedidos/', include(router.urls))
]

    
    #url(r'^category/$', CategoryViewSet),
    #url(r'^documenttype/$', DocumentTypeViewSet),
    #url(r'^invoice/$', InvoiceViewSet),
    #url(r'^order/$', OrdersViewSet),
    #url(r'^orderdetails/$', OrderDetailsViewSet),
    #url(r'^supplies/$', SuppliesViewSet),      


#urlpatterns = format_suffix_patterns(urlpatterns)