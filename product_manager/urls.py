from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from product_manager.core.views import delete, edit, list_products, new
from product_manager.core.api_views import (UserViewSet,
                                            GroupViewSet,
                                            ProductViewSet)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_products, name='list'),
    path('novo/', new, name='new'),
    path('editar/<int:product_id>', edit, name='edit'),
    path('deletar/<int:product_id>', delete, name='delete'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
