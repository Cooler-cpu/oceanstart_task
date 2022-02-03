from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin

from .models import Product
from .forms import ProductForm


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = ProductForm
