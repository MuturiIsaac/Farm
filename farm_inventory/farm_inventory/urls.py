# farm_inventory/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'inventory', views.InventoryItemViewSet)
router.register(r'livestock', views.LivestockViewSet)
router.register(r'crops', views.CropViewSet)
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'facilities', views.FacilityViewSet)
router.register(r'users', views.UserProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
