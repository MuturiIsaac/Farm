from django.contrib import admin

# Register your models here.
# inventory/admin.py

from django.contrib import admin
from .models import Category, Supplier, InventoryItem, Livestock, Crop, Equipment, Facility, UserProfile

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(InventoryItem)
admin.site.register(Livestock)
admin.site.register(Crop)
admin.site.register(Equipment)
admin.site.register(Facility)
admin.site.register(UserProfile)
